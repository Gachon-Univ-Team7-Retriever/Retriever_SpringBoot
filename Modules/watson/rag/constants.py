from server.db import DB, get_mongo_collection

# 모든 챗봇의 메타데이터를 가져와서 초기화.
chatbot_collection = get_mongo_collection(DB.NAME, DB.COLLECTION.CHATBOT)
chat_collection = get_mongo_collection(DB.NAME, DB.COLLECTION.CHANNEL.DATA)