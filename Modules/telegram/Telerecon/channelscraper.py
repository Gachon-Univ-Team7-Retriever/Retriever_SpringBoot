import asyncio
import re
from . import telegram_singleton
from .utils import *
from preprocess.extractor import dictionary
from server.db import get_mongo_client, db_name
from server.logger import logger

# 텔레그램 채널의 메세지가 마약 거래 채널인지 판단하는 함수
async def check_channel_content(invite_link) -> bool:
    try:
        logger.debug(f"Connecting to channel: {invite_link}")
        entity = await connect_channel(telegram_singleton.client, invite_link)
        if entity is None:
            logger.warning("Failed to connect to the channel.")
            return False

        # 메시지 확인
        post_count = 0
        suspicious_count = 0
        async for post in telegram_singleton.client.iter_messages(entity):
            post_count += 1
            if post.text:
                suspicious_count += sum([len(re.findall(re.escape(keyword), post.text)) for keyword in dictionary])
                if suspicious_count >= 3:
                    return True
                if post_count > 100:
                    return False


    except Exception as e:
        logger.error(f"An error occurred in check_channel_content(): {e}")
        return False

    return False


# 채널 내의 데이터를 스크랩하는 함수
async def scrape_channel_content(invite_link:str) -> dict:
    logger.debug(f"Connecting to channel: {invite_link}")

    content = []
    try:
        entity = await connect_channel(telegram_singleton.client, invite_link)
        if entity is None:
            logger.warning("Failed to connect to the channel.")
            return {"status": "warning",
                    "message": "Failed to connect to the channel."}
        # 메시지 스크랩
        post_count = 0

        async for message in telegram_singleton.client.iter_messages(entity):
            post_count += 1
            post_data = await process_message(entity, telegram_singleton.client, message)
            content.append(post_data)

            if post_count % 10 == 0:
                logger.info(f"{post_count} Posts is scraped from {invite_link}")

    except Exception as e:
        msg = f"An error occurred in scrape_channel_content(): {e}"
        logger.error(msg)
        return {"status": "error",
                "message": msg}

    try:
        # MongoDB client 생성
        mongo_client = get_mongo_client()
        collection_name = 'channel_data'
        # 컬렉션 선택
        collection = mongo_client[db_name][collection_name]

        # 수집된 채팅을 한 번에 모두 삽입. 이때 리스트 컴프리헨션으로 깊은 복사를 하지 않으면, MongoClient가 자동으로 content에 "_id"를 추가한 뒤에 삽입하기 때문에 원본 데이터가 변형됨.
        collection.insert_many([chat.copy() for chat in content])
    except Exception as exception:
        msg = f"Error occurred while inserting data into MongoDB: {exception}"
        logger.error(msg)
        return {"status": "error",
                "message": msg}
    else:
        msg = f"Archived a new chat in MongoDB - DB: {db_name}, collection: {collection_name}"
        logger.info(msg)
        return {"status": "success",
                "message": msg}

async def process_message(entity, client, message) -> dict:
    return {
        "channelId": entity.id,
        "timestamp": message.date,
        "text": message.text or "",
        "sender": extract_sender_info(message.sender),
        "views": message.views or None,
        "url": get_message_url_from_message(entity, message),
        "id": message.id,
        "media": await download_media(message, client),
    }


# 채널 데이터 수집을 동기적으로 실행하는 동기 래퍼(wrapper) 함수
def scrape(channel_name:str) -> dict:
    future = asyncio.run_coroutine_threadsafe(scrape_channel_content(channel_name), telegram_singleton.loop)
    return future.result()  # 블로킹 호출 (결과를 기다림)


# 채널 데이터 의심도 검증을 동기적으로 실행하는 동기 래퍼(wrapper) 함수
def check(channel_name:str) -> bool:
    future = asyncio.run_coroutine_threadsafe(check_channel_content(channel_name), telegram_singleton.loop)
    return future.result()  # 블로킹 호출 (결과를 기다림)
