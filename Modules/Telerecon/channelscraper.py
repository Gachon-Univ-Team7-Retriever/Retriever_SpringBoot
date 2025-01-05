import os
import asyncio
from . import details as ds
import base64
from telethon.sync import TelegramClient, types
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import CheckChatInviteRequest, ImportChatInviteRequest
from telethon.errors import UserAlreadyParticipantError

import pandas as pd
from colorama import Fore, Style

api_id = ds.apiID
api_hash = ds.apiHash
phone = ds.number

async def scrape_channel_content(invite_link):
    async with TelegramClient(phone, api_id, api_hash) as client:
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
                    return []
            else:
                # 일반적인 채널 이름 처리
                entity = await client.get_entity(invite_link)

            if not entity:
                print(f"{Fore.RED}Failed to retrieve entity for the channel.{Style.RESET_ALL}")
                return []

            # 메시지 스크랩
            content = []
            post_count = 0

            async for post in client.iter_messages(entity):
                post_count += 1

                text = post.text or ""
                media_base64 = None

                # 미디어 파일 다운로드
                if post.media:
                    if isinstance(post.media, (MessageMediaPhoto, MessageMediaDocument)):
                        try:
                            media_bytes = await client.download_media(
                                message=post,
                                file=bytes
                            )
                            media_base64 = base64.b64encode(media_bytes).decode('utf-8')
                        except Exception as e:
                            print(f"{Fore.RED}Failed to download media: {e}{Style.RESET_ALL}")

                # 메시지 보낸 날짜 및 시간
                message_date = post.date.strftime('%Y-%m-%d %H:%M:%S')

                # 기본적으로 모두 값 없음으로 초기화
                username = "N/A"
                first_name = "N/A"
                last_name = "N/A"
                user_id = "N/A"

                if sender := post.sender:
                    if isinstance(sender, types.User):
                        username = sender.username or "N/A"
                        first_name = sender.first_name or "N/A"
                        last_name = sender.last_name if sender.last_name else "N/A"
                        user_id = sender.id

                views = post.views or "N/A"
                message_url = f"https://t.me/{invite_link.split('+')[-1]}/{post.id}"

                content.append({
                    "date": message_date,
                    "text": text,
                    "username": username,
                    "first_name": first_name,
                    "last_name": last_name,
                    "user_id": user_id,
                    "views": views,
                    "url": message_url,
                    "media": media_base64,
                })

                if post_count % 10 == 0:
                    print(
                        f"{Fore.WHITE}{post_count} Posts scraped in {Fore.LIGHTYELLOW_EX}{invite_link}{Style.RESET_ALL}")

            return content

        except Exception as e:
            print(f"An error occurred: {Fore.RED}{e}{Style.RESET_ALL}")
            return []

def main(channel_name):
    # 비동기 데이터 수집 실행
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    content = loop.run_until_complete(scrape_channel_content(channel_name))
    return content

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
