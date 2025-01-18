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
    """
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(TelegramSingleton, cls).__new__(cls)
                    cls._instance.client = None
                    cls._instance.my_user_id = None
                    cls._instance._init_future = asyncio.Future()
        return cls._instance

    async def start_client(self, loop):
        self.client = TelegramClient(ds.number, ds.apiID, ds.apiHash, loop=loop)
        await self.client.start()
        logger.info("Telegram Client started.")
        return self.client

    async def get_me(self):
        if self.client is None:
            logger.error("Client is not initialized yet!")
            return None

        me = await self.client.get_me()
        logger.info(f"Your Telegram Client Name: {me.first_name}")
        logger.info(f"Your Telegram Client User ID: {me.id}")
        self.my_user_id = me.id
        return me.id

    def init(self, loop):
        """ 백그라운드 스레드에서 실행할 init() """
        # 비동기 작업을 순차적으로 실행
        loop.run_until_complete(self.start_client(loop))
        loop.run_until_complete(self.get_me())
        self._init_future.set_result(True)  # Future를 완료 상태로 설정
        logger.info("Telegram Client initialization complete.")
        print(f"in sub thread:{self._init_future}")

    def wait_for_init(self):
        """ 메인 스레드에서 백그라운드 작업이 끝날 때까지 대기 """
        loop = asyncio.get_event_loop()  # 메인 스레드의 이벤트 루프 사용
        print(f"in main thread:{self._init_future}")
        loop.run_until_complete(self._init_future)  # Future가 완료될 때까지 대기


def init_telegram():
    client = TelegramSingleton()
    loop = asyncio.new_event_loop()  # 백그라운드 스레드에서 새 이벤트 루프 생성
    asyncio.set_event_loop(loop)  # 새 루프를 설정
    client.init(loop)  # 백그라운드 스레드에서 init 실행
    loop.run_forever()  # 백그라운드에서 루프 계속 실행


# 별도의 스레드에서 실행
telegram_client = TelegramSingleton()
telegram_thread = threading.Thread(target=init_telegram, daemon=True)
telegram_thread.start()

# 메인 스레드에서 init() 완료까지 기다리기
telegram_client.wait_for_init()

# 그 외 다른 동작들
