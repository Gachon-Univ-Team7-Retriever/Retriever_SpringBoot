import asyncio
from telethon import events
from . import telegram_singleton
from .utils import *
from server.db import get_mongo_client, db_name
from server.logger import logger

from pymongo import MongoClient


# 특정 user id로 정기적인 심장박동 메세지를 보내는 비동기 함수
async def periodic_message(user_id):
    while True:
        await telegram_singleton.client.send_message(user_id, 'Periodic status message')
        await asyncio.sleep(43200)

def insert_data(collection, data):
    # 데이터 삽입
    result = collection.insert_one(data)
    # 삽입된 데이터의 ObjectId 출력
    logger.debug(f"Monitored Telegram chat inserted with ID: {result.inserted_id}")

async def monitor_channel(channel_username:str):
    # 새로운 이벤트 핸들러 정의 (채널별로 별도 핸들러를 생성하기 위해, 함수 내에서 동적으로 선언)
    async def event_handler(event):
        """ 메세지가 발생하면 반응하기 위한 핸들러의 비동기 함수 """
        chat = await event.get_chat()
        if chat and event.message: # 이벤트가 채팅방 이벤트이고, 메세지가 있을 때
            message, sender = event.message, await event.get_sender()
            message_text = message.message  # 메시지 텍스트 가져오기

            new_data = None
            try:
                # 삽입할 채팅 데이터 정의
                new_data = {
                    "channelId": chat.id,
                    "sender": extract_sender_info(sender), # 송신자 정보 가져오기
                    "url": get_message_url_from_event(event),
                    "id": event.message.id,
                    "text": message_text,
                    "timestamp": message.date, # datetime 형식의 메세지 발생 시간,
                    "media": await download_media(message, telegram_singleton.client)
                }

                logger.info(
                    f"Detected Message from {new_data['sender'].get('name')}: {message_text} at {new_data['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")

                # 메세지를 나에게 포워딩
                await telegram_singleton.client.forward_messages(telegram_singleton.my_user_id, event.message)
                logger.info(
                    f"Target(ID: {new_data['sender'].get('id')}, name: {new_data['sender'].get('name')}) spoke. time: {new_data['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            except Exception as exception:
                logger.error(f"Error in telegram event handler: {exception}")
            
            # 모니터링한 채팅을 MongoDB에 입력
            if new_data:
                try:
                    # MongoDB client 생성
                    mongo_client = get_mongo_client()
                    collection_name = 'channel_data'
                    # 컬렉션 선택
                    collection = mongo_client[db_name][collection_name]
                    # 데이터 삽입
                    collection.insert_one(new_data)
                except Exception as exception:
                    logger.error(f"Error occurred while inserting data into MongoDB: {exception}")
                else:
                    logger.info(f"Archived a new chat in MongoDB - DB: {db_name}, collection: {collection_name}")

    try:
        # 채널 엔티티 가져오기
        channel = await telegram_singleton.client.get_entity(channel_username)
        logger.debug(f"Monitoring channel - Channel Name: {channel.title}, Channel ID: {channel.id}")  # https://t.me/<channel_username>의 채널 ID 출력

        # 이벤트 핸들러 저장 및 등록
        event_handlers_map[channel_username] = event_handler
        telegram_singleton.client.add_event_handler(event_handler, events.NewMessage(chats=channel.id))
    except asyncio.CancelledError:
        logger.info(f"Task for {channel_username} was cancelled. Cleaning up...")
    except Exception as e:
        logger.error(f"Error in monitor_channel(): {e}")


# 특정 채널 모니터링을 시작하는 동기 함수
def start_monitoring(channel_username):
    try:
        if channel_username in monitoring_task_map:
            logger.warning(f"Already monitoring {channel_username}")
            return
        monitoring_task_map[channel_username] = asyncio.run_coroutine_threadsafe(monitor_channel(channel_username), telegram_singleton.loop)
        logger.info(f"Started monitoring {channel_username}")
    except Exception as e:
        logger.error(f"Error in start_monitoring(): {e}")


# 특정 채널 모니터링을 중단하는 함수
def stop_monitoring(channel_username):
    if channel_username in monitoring_task_map:
        # 1. 모니터링 Task 취소(모니터링 시작 Task가 실행되고 있었을 경우에 대비하기 위함)
        monitoring_task_map[channel_username].cancel()

        # 2. 등록된 이벤트 핸들러 제거
        if channel_username in event_handlers_map:
            telegram_singleton.client.remove_event_handler(event_handlers_map[channel_username])
            del event_handlers_map[channel_username]
        
        # 3. 모니터링 Task 제거
        del monitoring_task_map[channel_username]

        logger.info(f"Stopped monitoring {channel_username}")
    else:
        logger.warning(f"No active monitoring found for {channel_username}")


# 채팅 로그 파일 경로
log_file_path = "channel_messages.log"

# 메시지를 파일에 저장하는 비동기 함수
def save_message_to_file(sender_name, sender_id, message_text, timestamp):
    with open(log_file_path, "a", encoding="utf-8") as file:
        log_entry = f"[{timestamp}] Sender: {sender_name} (ID: {sender_id}), Message: {message_text}\n"
        file.write(log_entry)



monitoring_task_map, event_handlers_map  = {}, {}
# 백그라운드 작업 실행
telegram_singleton.loop.create_task(periodic_message(telegram_singleton.my_user_id))
