import os
import asyncio
import json
import re
from . import details as ds
import base64
from telethon.sync import TelegramClient, types
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from telethon.tl.functions.messages import CheckChatInviteRequest, ImportChatInviteRequest
from telethon.errors import UserAlreadyParticipantError
from preprocess.extractor import dictionary

import pandas as pd
from colorama import Fore, Style

api_id = ds.apiID
api_hash = ds.apiHash
phone = ds.number

async def connect_channel(client: TelegramClient, invite_link):
    entity = None
    try:
        # 초대 링크 처리
        if invite_link.startswith("+"):
            invite_hash = invite_link.split("+")[1]
            try:
                # 초대 링크 유효성 검사 및 채널 정보 가져오기
                invite_info = await client(CheckChatInviteRequest(invite_hash))

                if isinstance(invite_info, types.ChatInvite):
                    # 초대 링크가 유효하지만 아직 참여하지 않은 경우
                    print(f"{Fore.GREEN}Joining the channel via invite link...{Style.RESET_ALL}")
                    entity = await client(ImportChatInviteRequest(invite_hash))
                    print(f"{Fore.GREEN}Successfully joined the channel via invite link.{Style.RESET_ALL}")
                elif isinstance(invite_info, types.ChatInviteAlready):
                    # 이미 채널에 참여 중인 경우
                    entity = await client.get_entity(invite_info.chat)
                    print(f"{Fore.YELLOW}Already a participant in the channel. Retrieved entity.{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Failed to process invite link: {e}{Style.RESET_ALL}")
                return None
        else:
            # 일반적인 채널 이름 처리
            entity = await client.get_entity(invite_link)

        if not entity:
            print(f"{Fore.RED}Failed to retrieve entity for the channel.{Style.RESET_ALL}")
        return entity

    except Exception as e:
        print(f"An error occurred: {Fore.RED}{e}{Style.RESET_ALL}")
        return None


# 텔레그램 채널의 메세지가 마약 거래 채널인지 판단하는 함수
async def check_channel_content(invite_link) -> bool:
    async with TelegramClient(phone, api_id, api_hash) as client:
        try:
            entity = await connect_channel(client, invite_link)
            if entity is None:
                print("Failed to connect to the channel.")
                return False
            
            # 메시지 확인
            post_count = 0
            suspicious_count = 0
            async for post in client.iter_messages(entity):
                post_count += 1
                if post.text:
                    suspicious_count += sum([len(re.findall(re.escape(keyword), post.text)) for keyword in dictionary])
                    if suspicious_count >= 3:
                        return True
                    if post_count > 100:
                        return False


        except Exception as e:
            print(f"An error occurred: {Fore.RED}{e}{Style.RESET_ALL}")
            return False

        return False


# 채널 내의 데이터를 스크랩하는 함수
async def scrape_channel_content(invite_link):
    async with TelegramClient(phone, api_id, api_hash) as client:
        try:
            entity = await connect_channel(client, invite_link)
            if entity is None:
                print("Failed to connect to the channel.")
                return []
            # 메시지 스크랩
            content = []
            post_count = 0

            async for post in client.iter_messages(entity):
                post_count += 1
                post_data = await process_message(post, client, invite_link)
                content.append(post_data)

                if post_count % 10 == 0:
                    print(
                        f"{Fore.WHITE}{post_count} Posts scraped in {Fore.LIGHTYELLOW_EX}{invite_link}{Style.RESET_ALL}")

            return content

        except Exception as e:
            print(f"An error occurred: {Fore.RED}{e}{Style.RESET_ALL}")
            return []

async def process_message(post, client, invite_link):
    text = post.text or ""
    media_base64 = await download_media(post, client)
    message_date = post.date.strftime('%Y-%m-%d %H:%M:%S')

    sender_info = extract_sender_info(post.sender)

    return {
        "date": message_date,
        "text": text,
        **sender_info,
        "views": post.views or "N/A",
        "url": f"https://t.me/{invite_link.split('+')[-1]}/{post.id}",
        "media": media_base64,
    }

async def download_media(post, client):
    if post.media and isinstance(post.media, (MessageMediaPhoto, MessageMediaDocument)):
        try:
            media_bytes = await client.download_media(
                message=post,
                file=bytes
            )
            return base64.b64encode(media_bytes).decode('utf-8')
        except Exception as e:
            print(f"Failed to download media: {e}")
            return None
    return None

def extract_sender_info(sender):
    if sender and isinstance(sender, types.User):
        return {
            "username": sender.username or "N/A",
            "first_name": sender.first_name or "N/A",
            "last_name": sender.last_name if sender.last_name else "N/A",
            "user_id": sender.id,
        }
    return {
        "username": "N/A",
        "first_name": "N/A",
        "last_name": "N/A",
        "user_id": "N/A",
    }


# 채널 데이터 수집을 동기적으로 실행하는 동기 래퍼(wrapper) 함수
def scrape(channel_name:str) -> list[dict]:
    # 비동기 데이터 수집 실행 후 반환
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(scrape_channel_content(channel_name))


# 채널 데이터 의심도 검증을 동기적으로 실행하는 동기 래퍼(wrapper) 함수
def check(channel_name:str) -> bool:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(check_channel_content(channel_name))

# async def main():
#     try:
#         channel_name = input(
#             f"{Fore.CYAN}Please enter a target Telegram channel (e.g., https://t.me/{Fore.LIGHTYELLOW_EX}your_channel{Style.RESET_ALL}):\n")
#         print(f'You entered "{Fore.LIGHTYELLOW_EX}{channel_name}{Style.RESET_ALL}"')
#         answer = input('Is this correct? (y/n)')
#         if answer != 'y':
#             return
#
#         output_directory = sanitizer.sanitize_filename(f"Collection/{channel_name}")
#         if not os.path.exists(output_directory):
#             os.makedirs(output_directory)
#
#         csv_filename = sanitizer.sanitize_filename(f'{output_directory}/{channel_name}_messages.csv')
#         print(f'Scraping content from {Fore.LIGHTYELLOW_EX}{channel_name}{Style.RESET_ALL}...')
#
#         content = await scrape_channel_content(channel_name)
#
#         if content:
#             df = pd.DataFrame(content, columns=['Datetime', 'Text', 'Username', 'First Name', 'Last Name', 'User ID', 'Views',
#                                                 'Message URL', 'Media File Path'])
#             try:
#                 df.to_csv(csv_filename, index=False)
#                 print(
#                     f'Successfully scraped and saved content to {Fore.LIGHTYELLOW_EX}{csv_filename}{Style.RESET_ALL}.')
#             except Exception as e:
#                 print(f"An error occurred while saving to CSV: {Fore.RED}{e}{Style.RESET_ALL}")
#         else:
#             print(f'{Fore.RED}No content scraped.{Style.RESET_ALL}')
#
#     except Exception as e:
#         print(f"An error occurred: {Fore.RED}{e}{Style.RESET_ALL}")


# if __name__ == '__main__':
#     asyncio.run(main())
