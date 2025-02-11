import asyncio
import typing
from pymongo.errors import DuplicateKeyError

from server.db import get_mongo_client, DB
from server.logger import logger
from .channelscraper import ChannelContentMethods
from .monitor import ChannelContentMonitorMethods
if typing.TYPE_CHECKING:
    from .manager import TelegramManager

class ChannelMethods(ChannelContentMethods, ChannelContentMonitorMethods):
    def get_channel_info(self:'TelegramManager', channel_key:typing.Union[int, str]) -> dict:
        # MongoDB client 생성
        mongo_client, collection_name = get_mongo_client(), DB.COLLECTION.CHANNEL.INFO
        collection = mongo_client[DB.NAME][collection_name]  # 컬렉션 선택

        entity = asyncio.run_coroutine_threadsafe(self.connect_channel(channel_key), self.loop).result()

        channel_info = {
            "id": entity.id,
            "title": entity.title,
            "username": entity.username,
            "restricted": entity.restricted, # 채널에 제한이 있는지 여부 (boolean)
            "date": entity.date, # 채널이 생성된 일시 (datetime.datetime)
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