import asyncio
import typing

from server.db import get_mongo_client, db_name
from server.logger import logger
from .channelscraper import ChannelContentMethods
from .monitor import ChannelContentMonitorMethods
if typing.TYPE_CHECKING:
    from .manager import TelegramManager

class ChannelMethods(ChannelContentMethods, ChannelContentMonitorMethods):
    def get_channel_info(self:'TelegramManager', channel_key:typing.Union[int, str]) -> dict:
        # MongoDB client 생성
        mongo_client, collection_name = get_mongo_client(), 'channel_data'
        collection = mongo_client[db_name][collection_name]  # 컬렉션 선택

        entity = asyncio.run_coroutine_threadsafe(self.connect_channel(channel_key), self.loop).result()

        channel_info = {
            "id": entity.id,
            "title": entity.title,
            "username": entity.username,
            "restricted": entity.restricted, # 채널에 제한이 있는지 여부 (boolean)
            "date": entity.date, # 채널이 생성된 일시 (datetime.datetime)
        }
        try:
            collection.insert_one(channel_info)  # 데이터 삽입
        except Exception as exception:
            logger.error(f"Error occurred while inserting data into MongoDB: {exception}")
        else:
            logger.info(f"Archived a new channel metadata in MongoDB - DB: {db_name}, collection: {collection_name}")

        return channel_info