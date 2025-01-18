import asyncio
import threading
import time

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
                    cls._instance._loop = None  # 🔧 (수정됨) 이벤트 루프 저장
                    cls._instance._init_future = None  # 🔧 (수정됨) Future를 늦게 생성
        return cls._instance

    async def start_client(self):
        """ 텔레그램 클라이언트 시작 """
        self.client = TelegramClient(ds.number, ds.apiID, ds.apiHash, loop=self._loop)
        await self.client.start()
        logger.info("Telegram Client started.")
        return self.client

    async def get_me(self):
        """ 사용자 정보 가져오기 """
        if self.client is None:
            logger.error("Client is not initialized yet!")
            return None

        me = await self.client.get_me()
        logger.info(f"Your Telegram Client Name: {me.first_name}")
        logger.info(f"Your Telegram Client User ID: {me.id}")
        self.my_user_id = me.id
        return me.id

    async def _init_async(self):
        """ 비동기 초기화 (Future 설정 포함) """
        await self.start_client()
        await self.get_me()
        self._init_future.set_result(True)  # Future 완료 설정
        logger.info("Telegram Client initialization complete.")
        print(f"[DEBUG] in sub thread: Future state -> {self._init_future.done()}")  # 🔧 (디버깅 추가)

    def init(self, loop):
        """ 백그라운드 스레드에서 실행할 init() """
        self._loop = loop  # 🔧 (수정됨) 현재 스레드의 이벤트 루프 저장
        self._init_future = loop.create_future()  # 🔧 (수정됨) 현재 루프에서 Future 생성
        loop.run_until_complete(self._init_async())  # 클라이언트 비동기 실행

    def wait_for_init(self):
        """ 메인 스레드에서 백그라운드 작업이 끝날 때까지 대기 """
        print("[DEBUG] Waiting for initialization...")

        # 🔧 (수정됨) Future가 생성될 때까지 대기
        while self._init_future is None:
            time.sleep(0.1)

        print(f"[DEBUG] in main thread: Future state before wait -> {self._init_future.done()}")

        if self._init_future.done():
            print("[DEBUG] Initialization already completed.")
            return

        # 🔧 (수정됨) 새로운 코루틴을 만들어서 asyncio.run_coroutine_threadsafe() 실행
        async def wait_for_future():
            await self._init_future  # Future가 완료될 때까지 대기

        future = asyncio.run_coroutine_threadsafe(wait_for_future(), self._loop)
        future.result()  # Future 완료될 때까지 대기

        print(f"[DEBUG] in main thread: Future state after wait -> {self._init_future.done()}")


def init_telegram():
    """ 백그라운드 스레드에서 실행되는 초기화 함수 """
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
