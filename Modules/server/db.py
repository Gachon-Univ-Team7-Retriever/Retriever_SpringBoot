import os
import pymongo
from dotenv import load_dotenv
from pymongo.synchronous.collection import Collection
from pymongo.synchronous.database import Database

load_dotenv()

def get_mongo_connection_string() -> str:
    return (f"mongodb://{os.environ.get('DB_USERNAME')}"
            f":{os.environ.get('DB_PASSWORD')}"
            f"@{os.environ.get('DB_IP')}"
            f":{os.environ.get('DB_PORT')}/")

def get_mongo_client() -> pymongo.MongoClient:
    return pymongo.MongoClient(get_mongo_connection_string())

def get_mongo_database(database_name) -> Database:
    return get_mongo_client()[database_name]

def get_mongo_collection(db, collection) -> Collection:
    return get_mongo_database(db)[collection]

class Database:
    class Collection:
        class Channel:
            INFO = "channel_info"
            DATA = "channel_data"
            SIMILARITY = "channel_similarity"
        CHANNEL = Channel
        CHATBOT = "chat_bot"
    COLLECTION = Collection
    NAME = os.environ.get('DB_NAME')
DB = Database