import asyncio
from telethon import TelegramClient, events
from telegram.Telerecon import details as ds
from server.logger import logger

# details 모듈에서 가져오기
api_id = ds.apiID
api_hash = ds.apiHash
phone = ds.number

client = TelegramClient(phone, api_id, api_hash)
client.start()
logger.info("Telegram Client started.")
async def init():
    me = await client.get_me() # 현재 사용자의 정보 가져오기
    logger.info(f"Your Telegram Client Name: {me.first_name}")
    logger.info(f"Your Telegram Client User ID: {me.id}")  # 사용자 ID 출력

    return me.id

my_user_id = client.loop.run_until_complete(init())