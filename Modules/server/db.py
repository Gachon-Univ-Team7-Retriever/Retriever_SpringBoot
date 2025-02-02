import os
import pymongo
from dotenv import load_dotenv
load_dotenv()

def get_mongo_client() -> pymongo.MongoClient:
    return pymongo.MongoClient(f"mongodb://{os.environ.get('DB_USERNAME')}"
                               f":{os.environ.get('DB_PASSWORD')}"
                               f"@{os.environ.get('DB_IP')}"
                               f":{os.environ.get('DB_PORT')}/")

db_name = os.environ.get('DB_NAME')