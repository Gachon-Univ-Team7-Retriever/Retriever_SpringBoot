import asyncio
import typing
from telethon import events
from .utils import *
from server.db import get_mongo_client, DB
from server.logger import logger

if typing.TYPE_CHECKING:
    from .manager import TelegramManager


# 채팅 로그 파일 경로
log_file_path = "channel_messages.log"

class ChannelContentMonitorMethods:
    def __init__(self):
        self.monitoring_task_map, self.event_handlers_map = {}, {}
        super().__init__()

    # 특정 user id로 정기적인 심장박동 메세지를 보내는 비동기 함수 (현재 사용되지 않음)
    async def periodic_message(self:'TelegramManager', user_id):
        while True:
            await self.client.send_message(user_id, 'Periodic status message')
            await asyncio.sleep(43200)
    
    async def monitor_channel(self:'TelegramManager', channel_key:typing.Union[int, str]):
        # 새로운 이벤트 핸들러 정의 (채널별로 별도 핸들러를 생성하기 위해, 함수 내에서 동적으로 선언)
        async def event_handler(event):
            """ 메세지가 발생하면 반응하기 위한 핸들러의 비동기 함수 """
            # MongoDB client 생성
            mongo_client, collection_name = get_mongo_client(), DB.COLLECTION.CHANNEL.DATA
            collection = mongo_client[DB.NAME][collection_name]  # 컬렉션 선택
    
            chat = await event.get_chat()
            # 이벤트가 채팅방 이벤트이고, 메세지가 있고, 해당 메세지가 아직 수집되지 않은 것일 때에만
            if chat and event.message:
                message, sender = event.message, await event.get_sender()
                message_text = message.message  # 메시지 텍스트 가져오기
                if not collection.find_one({"channelId": chat.id, "id": message.id}):
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
                            "media": await download_media(message, self.client)
                        }
    
                        logger.info(
                            f"Detected Message from {new_data['sender'].get('name')}: {message_text} at {new_data['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
    
                        # 메세지를 나에게 포워딩
                        await self.client.forward_messages(self.my_user_id, event.message)
                        logger.info(
                            f"Target(ID: {new_data['sender'].get('id')}, name: {new_data['sender'].get('name')}) spoke. time: {new_data['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
                    except Exception as exception:
                        logger.error(f"Error in telegram event handler: {exception}")
                    if new_data:
                        try:
                            collection.insert_one(new_data) # 데이터 삽입
                        except Exception as exception:
                            logger.error(f"Error occurred while inserting data into MongoDB: {exception}")
                        else:
                            logger.info(f"Archived a new chat in MongoDB - DB: {DB.NAME}, collection: {collection_name}")
                else:
                    logger.warning(
                        f"MongoDB collection already has same unique index of a chat(channelId: {chat.id}, id: {message.id})")
    
        try:
            # 채널 엔티티 가져오기
            channel = await self.connect_channel(channel_key)
            logger.debug(f"Monitoring channel - Channel Name: {channel.title}, Channel ID: {channel.id}")  # https://t.me/<channel_username>의 채널 ID 출력
    
            # 이벤트 핸들러 저장 및 등록
            self.event_handlers_map[channel_key] = event_handler
            self.client.add_event_handler(event_handler, events.NewMessage(chats=channel.id))
        except asyncio.CancelledError:
            logger.info(f"Task for {channel_key} was cancelled. Cleaning up...")
        except Exception as e:
            logger.error(f"Error in monitor_channel(): {e}")
    
    
    # 특정 채널 모니터링을 시작하는 동기 함수
    def start_monitoring(self:'TelegramManager', channel_key:typing.Union[int, str]):
        try:
            if channel_key in self.monitoring_task_map:
                logger.warning(f"Already monitoring {channel_key}")
                return
            self.monitoring_task_map[channel_key] = asyncio.run_coroutine_threadsafe(
                self.monitor_channel(channel_key), self.loop)
            logger.info(f"Started monitoring {channel_key}")
        except Exception as e:
            logger.error(f"Error in start_monitoring(): {e}")
    
    
    # 특정 채널 모니터링을 중단하는 함수
    def stop_monitoring(self:'TelegramManager', channel_key:typing.Union[int, str]):
        if channel_key in self.monitoring_task_map:
            # 1. 모니터링 Task 취소(모니터링 시작 Task가 실행되고 있었을 경우에 대비하기 위함)
            self.monitoring_task_map[channel_key].cancel()
    
            # 2. 등록된 이벤트 핸들러 제거
            if channel_key in self.event_handlers_map:
                self.client.remove_event_handler(self.event_handlers_map[channel_key])
                del self.event_handlers_map[channel_key]
            
            # 3. 모니터링 Task 제거
            del self.monitoring_task_map[channel_key]
    
            logger.info(f"Stopped monitoring {channel_key}")
        else:
            logger.warning(f"No active monitoring found for {channel_key}")

    
# 메시지를 파일에 저장하는 비동기 함수
def save_message_to_file(sender_name, sender_id, message_text, timestamp):
    with open(log_file_path, "a", encoding="utf-8") as file:
        log_entry = f"[{timestamp}] Sender: {sender_name} (ID: {sender_id}), Message: {message_text}\n"
        file.write(log_entry)
