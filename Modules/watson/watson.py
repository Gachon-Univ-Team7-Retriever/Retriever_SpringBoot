from flask import Blueprint, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

from server.logger import logger
from .rag import BaseWatson, LangGraphMethods, VectorStoreMethods, chatbot_collection

watson_bp = Blueprint("watson", __name__)
CORS(watson_bp)  # CORS 활성화

class AutoCreateInstances(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances = {}
        for document in chatbot_collection.find():
            cls._instances[document.get('id')] = cls(bot_id=document.get('id'))

        logger.info(f"데이터베이스에 있는 챗봇을 모두 로드했습니다. 로드된 챗봇: {list(cls._instances.keys())}")

class Watson(BaseWatson, VectorStoreMethods, LangGraphMethods, metaclass=AutoCreateInstances):
    def generate_response(self, message):
        return f"Watson 응답: {message}"

    def reset_conversation(self):
        return "대화가 초기화되었습니다."