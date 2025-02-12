import asyncio
import typing
import datetime
from pymongo.errors import DuplicateKeyError

from server.db import DB, get_mongo_collection
from server.logger import logger
from .channelscraper import ChannelContentMethods
from .monitor import ChannelContentMonitorMethods
if typing.TYPE_CHECKING:
    from .manager import TelegramManager

class ChannelMethods(ChannelContentMethods, ChannelContentMonitorMethods):
    def get_channel_info(self:'TelegramManager', channel_key:typing.Union[int, str]) -> dict:
        # MongoDB client 생성
        collection_name = DB.COLLECTION.CHANNEL.INFO
        collection = get_mongo_collection(DB.NAME, collection_name)  # 컬렉션 선택
        entity = asyncio.run_coroutine_threadsafe(self.connect_channel(channel_key), self.loop).result()

        channel_info = {
            "id": entity.id,
            "title": entity.title,
            "username": entity.username,
            "restricted": entity.restricted, # 채널에 제한이 있는지 여부 (boolean)
            "startedAt": entity.date, # 채널이 생성된 일시 (datetime.datetime)
            "discoveredAt": datetime.datetime.now(), # 채널이 처음으로 발견된 일시
            "updatedAt": datetime.datetime.now(), # 채널의 업데이트를 마지막으로 확인한 일시
        }
        try:
            collection.insert_one(channel_info.copy())  # 데이터 삽입. copy()를 하지 않으면 mongoClient가 channel_info 원본 딕셔너리에 ObjectId를 삽입함.
        except DuplicateKeyError:
            logger.warning(f"Tried to archive a channel which is already archived. Channel ID: {entity.id}, title: {entity.title}")
        except Exception as exception:
            logger.error(f"Error occurred while inserting data into MongoDB: {exception}")
        else:
            logger.info(f"Archived a new channel metadata in MongoDB - DB: {DB.NAME}, collection: {collection_name}")

        return channel_info


def is_channel_empty(channel_id) -> bool:
    """채널 ID에 해당하는 채널의 채팅 데이터가 있는지 여부를 조사하는 함수. 데이터가 없을 때 True 반환."""
    chat_collection = get_mongo_collection(DB.NAME, DB.COLLECTION.CHANNEL.DATA)
    # 채널 ID를 기준으로 모든 채팅을 찾아서 각 채팅의 채팅 ID를 리스트로 생성
    return False if chat_collection.find_one({"channelId": channel_id}) else True