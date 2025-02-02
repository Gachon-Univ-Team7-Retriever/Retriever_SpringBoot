import asyncio
import threading

from telethon import TelegramClient
from telegram.Telerecon import details as ds
from server.logger import logger

# details 모듈에서 가져오기
api_id = ds.apiID
api_hash = ds.apiHash
phone = ds.number


class TelegramSingleton:
    """
        텔레그램 클라이언트를 백그라운드 스레드에서 생성하고, 그 클라이언트를 다른 모듈에서도 활용하기 위한 싱글톤 객체.

        싱글톤 객체의 주요 특징

        1. 단 하나의 인스턴스
        - 싱글톤 클래스는 인스턴스를 하나만 생성하며, 동일한 인스턴스가 여러 번 호출되더라도 동일한 객체를 반환한다.
        - 이를 통해 메모리 낭비를 방지하고, 프로그램의 여러 부분에서 같은 객체를 일관되게 사용할 수 있다.

        2. 전역적 접근
        - 싱글톤 인스턴스는 어디서든지 접근이 가능하며, 보통 애플리케이션 전체에서 공유된다.
        - 데이터베이스 연결, 로그 파일, 애플리케이션 설정 등을 다룰 때 아주 유용하다.

        3. 지연 초기화 (Lazy Initialization)
        - 싱글톤 객체는 필요할 때(즉, 처음 호출될 때)만 인스턴스를 생성하는 방식으로 초기화되며, 초기화가 늦춰지는 경우가 많다. 때문에 메모리 자원을 절약하는 데 유리하다.

        Telethon 라이브러리의 TelegramClient 객체는 비동기 작업을 수행하기 위해 자체적으로 Event Loop를 이용한다.
        Asyncio의 구조상 Event Loop는 Thread-specific 하기 때문에 새로운 스레드에서 비동기 작업을 Asyncio로 실행하려면 그 스레드에서 새로운 Event Loop를 생성하고 실행해야 한다.
        Flask 서버는 새로운 요청이 들어올 때마다 Thread를 새로 생성해서 대응하므로, 각 Thread에서 Telethon의 비동기 작업을 수행하려면
        그 Thread에서 따로 Event Loop를 생성한 후 생성된 Event Loop에서 작업을 수행해야 한다는 뜻이다.
        그러나, Telethon 라이브러리에서는 Deadlock 현상을 방지하기 위해
        TelegramClient이 생성 및 연결되었을 당시의 Thread와 Event Loop과 현재 작업을 수행하는 Thread와 Event Loop이 완벽히 똑같지 않으면 오류를 내도록 구현되어 있다.
        (TelegramClient를 요청을 받을 때마다 각 작업의 스레드마다 생성하는 방식을 사용할 수도 있지만 유지보수가 어려워지고,
        세션 파일은 한 스레드만 이용할 수 있기 때문에 Thread.Lock을 이용해서 한 스레드가 Client를 이용 중에는 다른 스레드가 이용할 수 없도록 막아야 하므로 성능의 상당부분을 포기하게 된다.)

        즉, 이 문제를 해결하려면 특정 스레드에서 Telegram Client와 Event Loop를 생성, 그 스레드가 계속 운용되도록 하고,
        Flask에서 요청에 응답하기 위해 생성한 스레드가 해당 스레드에 요청을 보내고 그 결과를 받아오게 해야 하는데,
        이 작업을 가능하게 해주는 기능은 asyncio.run_coroutine_threadsafe(coroutine, loop) 뿐이다.

        이때, 다른 스레드에서 Telegram Client가 동작하는 스레드에 asyncio.run_coroutine_threadsafe 로 요청을 보내려면
        해당 스레드에서 Telegram Client의 Loop가 계속해서 작동하고 있어야 하는데,
        이를 위해 메인 스레드에서 loop.run_forever()를 사용하면 Flask 서버의 코드에 도달하지 않으므로,
        백그라운드 스레드를 만들고 그 스레드에서 Telegram Client와 Event Loop를 생성한다.

        이 때, 다른 모듈에서 Telegram Client를 안정적으로 참조하려면 메인 스레드에서도 client를 선언, 다른 스레드에서도 client를 선언해야 한다.
        race condition 등의 문제를 사전에 차단하려면 전역 변수 등의 방식보다
        싱글톤 객체(Singleton)이 더 안정적이고 유지보수에 용이하며 코드도 깔끔하다고 판단하여, 싱글톤 객체를 도입하였다.
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(TelegramSingleton, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        # 현재 실행 흐름이 백그라운드 스레드일 경우, 루프를 만들고 클라이언트를 초기화한다.
        if threading.current_thread() is not threading.main_thread():
            background_loop = asyncio.new_event_loop()  # 백그라운드 스레드에서 새 이벤트 루프 생성
            asyncio.set_event_loop(background_loop)  # 새 루프를 설정

            self.loop = background_loop
            self.client = background_loop.run_until_complete(self.start_client())
            self.my_user_id = background_loop.run_until_complete(self.get_me())
        else:
            # 만약 현재 실행 흐름이 백그라운드 스레드가 아닐 경우(메인 스레드일 경우), 기존 값이 있으면 그대로 두고 없으면 None으로 초기화한다.
            self.client = getattr(self, "client", None)
            self.my_user_id = getattr(self, "my_user_id", None)
            self.loop = getattr(self, "loop", None)

    async def start_client(self):
        """ 텔레그램 클라이언트를 초기화하고 시작, 초기화된 클라이언트를 반환하는 메서드 """
        if threading.current_thread() is threading.main_thread():
            error_message = "Telegram Singleton을 메인 스레드에서 실행하고 있습니다. Flask 서버가 제대로 실행되지 않을 수 있습니다."
            logger.warning(error_message)
            raise RuntimeWarning(error_message)
        if not self.loop:
            error_message = "Loop를 생성하지 않은 상태로 텔레그램 클라이언트를 시작하려고 시도했습니다."
            logger.critical(error_message)
            raise ValueError(error_message)
        elif not isinstance(self.loop, asyncio.AbstractEventLoop):
            error_message = "Loop가 이벤트 루프 객체(AbstractEventLoop)가 아닌 상태로 텔레그램 클라이언트를 시작하려고 시도했습니다."
            logger.critical(error_message)
            raise TypeError(error_message)

        self.client = TelegramClient(ds.number, ds.apiID, ds.apiHash, loop=self.loop)
        await self.client.start()
        logger.info("Telegram Client started.")
        return self.client

    async def get_me(self):
        """ 현재 클라이언트에서 사용자 정보를 가져오는 메서드 """
        if self.client is None:
            error_message = "텔레그램 클라이언트가 아직 초기화되지 않은 상태에서 클라이언트의 유저 정보를 가져오려고 시도했습니다."
            logger.critical(error_message)
            raise ValueError(error_message)

        me = await self.client.get_me()
        logger.info(f"Your Telegram Client Name: {me.first_name}")
        logger.info(f"Your Telegram Client User ID: {me.id}")
        self.my_user_id = me.id
        return me.id

singleton_ready = threading.Event()  # 이벤트 객체 생성
telegram_singleton = TelegramSingleton()


def init_telegram_singleton():
    """ 백그라운드 스레드에서 실행되는 텔레그램 클라이언트 초기화 함수 """
    telegram_singleton = TelegramSingleton() # 여기서는 백그라운드 호출이기 때문에, Singleton 객체에서
    singleton_ready.set()  # 이벤트 트리거: (백그라운드 스레드에서) 싱글톤의 준비가 완료되었음을 이벤트로 알림
    try:
        telegram_singleton.loop.run_forever()  # 백그라운드에서 루프 계속 실행
    finally:
        telegram_singleton.client.disconnect()


# 별도의 스레드에서 실행
threading.Thread(target=init_telegram_singleton, daemon=True).start()
singleton_ready.wait()  # 싱글톤의 텔레그램 클라이언트가 전부 준비될 때까지 대기
