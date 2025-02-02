from telethon.sync import TelegramClient, types
from telethon.tl.functions.messages import CheckChatInviteRequest, ImportChatInviteRequest
import telethon
from telethon.sync import types
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from server.logger import logger
from typing import Optional

async def connect_channel(client: TelegramClient, invite_link):
    entity = None
    try:
        # 초대 링크 처리
        if invite_link.startswith("+"):
            invite_hash = invite_link.split("+")[1]
            try:
                # 초대 링크 유효성 검사 및 채널 정보 가져오기
                invite_info = client(CheckChatInviteRequest(invite_hash))

                if isinstance(invite_info, types.ChatInvite):
                    # 초대 링크가 유효하지만 아직 참여하지 않은 경우
                    logger.debug(f"Joining the channel via invite link...")
                    entity = await client(ImportChatInviteRequest(invite_hash))
                    logger.debug(f"Successfully joined the channel via invite link.")
                elif isinstance(invite_info, types.ChatInviteAlready):
                    # 이미 채널에 참여 중인 경우
                    entity = await client.get_entity(invite_info.chat)
                    logger.warning(f"Already a participant in the channel. Retrieved entity.")
            except Exception as e:
                logger.error(f"Failed to process invite link: {e}")
                return None
        else:
            # 일반적인 채널 이름 처리
            entity = await client.get_entity(invite_link)

        if not entity:
            logger.warning(f"Failed to retrieve entity for the channel.")

        return entity

    except Exception as e:
        logger.error(f"An error occurred in connect_channel(): {e}")
        return None

def extract_sender_info(sender):
    if sender and isinstance(sender, types.User):
        return {
            "type": "user",
            "name": sender.username or None,
            "firstName": sender.first_name or None,
            "lastName": sender.last_name or None,
            "id": sender.id,
        }
    elif sender and isinstance(sender, types.Channel):
        return {
            "type": "channel",
            "name": sender.title or None,
            "id": sender.id,
        }
    return {
        "type": "unknown",
        "name": None,
        "id": None
    }


def get_message_url_from_event(event):
    if event.chat:
        message_id = event.message.id  # 메시지 ID

        if event.chat.username:  # 공개 채널
            channel_username = event.chat.username
            return f"https://t.me/{channel_username}/{message_id}"
        else:  # 비공개 채널
            channel_id = abs(event.chat.id)  # 절댓값 사용
            return f"https://t.me/c/{channel_id}/{message_id}"

    return None  # 채널 정보 없음


def get_message_url_from_message(entity, message):
    if message.id:
        if entity.username: # 공개(public) 채널
            return f"https://t.me/{entity.username}/{message.id}"
        else: # 비공개(private) 채널
            return f"https://t.me/c/{str(entity.id).replace('-100', '')}/{message.id}"

    return None  # 채널 정보 없음


import base64
async def download_media(message, client) -> Optional[str]:
    if message.media and isinstance(message.media, (MessageMediaPhoto, MessageMediaDocument)):
        try:
            media_bytes = await client.download_media(
                message=message,
                file=bytes
            )
            return base64.b64encode(media_bytes).decode('utf-8')
        except Exception as e:
            logger.error(f"Failed to download media: {e}")
            return None
    return None
