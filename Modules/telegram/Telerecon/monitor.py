from telethon import TelegramClient, events
from datetime import datetime
import asyncio
import details as ds

# details 모듈에서 가져오기
api_id = ds.apiID
api_hash = ds.apiHash
phone = ds.number
channel_username = "Hyde_Sandbox"

# 채팅 로그 파일 경로
log_file_path = "channel_messages.log"

print("Application run...")

client = TelegramClient(phone, api_id, api_hash)

print("Instance created!")

# 메시지를 파일에 저장하는 함수
def save_message_to_file(sender_name, sender_id, message_text, timestamp):
    with open(log_file_path, "a", encoding="utf-8") as file:
        log_entry = f"[{timestamp}] Sender: {sender_name} (ID: {sender_id}), Message: {message_text}\n"
        file.write(log_entry)

async def periodic_message(my_user_id):
    while True:
        await client.send_message(my_user_id, 'Periodic status message')
        await asyncio.sleep(43200)

async def main():
    await client.start()
    print("Client started.")
    target_channel_id = None
    try:
        # 채널 엔티티 가져오기
        channel = await client.get_entity(channel_username)
        print(f"Channel Name: {channel.title}")
        print(f"Channel ID: {channel.id}")  # https://t.me/<channel_username>의 채널 ID 출력
        target_channel_id = channel.id
    except Exception as e:
        print(f"Error: {e}")

    me = await client.get_me()  # 현재 사용자의 정보 가져오기
    print(f"Your Name: {me.first_name}")
    print(f"Your User ID: {me.id}")  # 사용자 ID 출력
    my_user_id = me.id

    async def my_event_handler(event):
        if event.sender_id is not None:
            now = datetime.now()
            print("Target spoke", "time:", now.date(), now.time())
            await client.forward_messages(my_user_id, event.message)

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_text = event.message.message  # 메시지 텍스트 가져오기
            try:
                # 송신자 정보 가져오기
                sender = await event.get_sender()
                sender_name = sender.username if sender.username else "Unknown"
                sender_id = event.sender_id
                print(f"Message from {sender_name}: {message_text} at {now}")
                # 메시지를 파일에 저장
                save_message_to_file(sender_name, sender_id, message_text, now)
            except Exception as e:
                print(f"Error retrieving sender info: {e}")

    client.loop.create_task(periodic_message(my_user_id))
    client.add_event_handler(my_event_handler, events.NewMessage(chats=target_channel_id))
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
