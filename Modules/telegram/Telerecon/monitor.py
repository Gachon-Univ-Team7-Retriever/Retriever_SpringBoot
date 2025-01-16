import asyncio
from datetime import datetime
from telethon import events
from . import my_user_id, client
from server.logger import logger
import threading

loop = asyncio.get_event_loop()
def run_event_loop():
    """ 백그라운드 스레드에서 모니터링을 관리하는 이벤트 루프 실행. """
    asyncio.set_event_loop(loop)
    loop.run_forever()

# 이벤트 루프 실행용 백그라운드 스레드 시작
threading.Thread(target=run_event_loop, daemon=True).start()

# 특정 user id로 정기적인 심장박동 메세지를 보내는 비동기 함수
async def periodic_message(user_id):
    while True:
        await client.send_message(user_id, 'Periodic status message')
        await asyncio.sleep(43200)

async def monitor_channel(channel_username):
    # 새로운 이벤트 핸들러 정의 (채널별로 별도 핸들러 생성)
    async def event_handler(event):
        await my_event_handler(event)

    try:
        # 채널 엔티티 가져오기
        channel = await client.get_entity(channel_username)
        logger.debug(f"Monitoring channel - Channel Name: {channel.title}, Channel ID: {channel.id}")  # https://t.me/<channel_username>의 채널 ID 출력

        # 이벤트 핸들러 저장 및 등록
        event_handlers_map[channel_username] = event_handler
        client.add_event_handler(event_handler, events.NewMessage(chats=channel.id))
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
        monitoring_task_map[channel_username] = asyncio.run_coroutine_threadsafe(monitor_channel(channel_username), loop)
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
            client.remove_event_handler(event_handlers_map[channel_username])
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

async def my_event_handler(event):
    if event.sender_id is not None:
        try:
            now = datetime.now()
            message_text = event.message.message  # 메시지 텍스트 가져오기
            # 송신자 정보 가져오기
            sender = await event.get_sender()
            sender_name = sender.username if sender.username else "Unknown"
            sender_id = event.sender_id

            logger.info(f"Detected Message from {sender_name}: {message_text} at {now.strftime('%Y-%m-%d %H:%M:%S')}")
            # 메시지를 파일에 저장
            save_message_to_file(sender_name, sender_id, message_text, now.strftime("%Y-%m-%d %H:%M:%S"))

            # 메세지를 나에게 포워딩
            await client.forward_messages(my_user_id, event.message)
            logger.info(f"Target(ID: {sender_id}, name: {sender_name}) spoke. time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            logger.error(f"Error retrieving sender info: {e}")


monitoring_task_map, event_handlers_map  = {}, {}
# 백그라운드 작업 실행
client.loop.create_task(periodic_message(my_user_id))
