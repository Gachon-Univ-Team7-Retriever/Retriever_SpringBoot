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


@watson_bp.route("/watson/c", methods=["POST"])
def chat():
    data = request.json
    action = data.get("action")
    channel_ids = data.get("channel_ids")
    scope = data.get("scope")

    logger.info(f"Received request: action={action}, channel_ids={channel_ids}, scope={scope}")

    if not channel_ids or not scope:
        return jsonify(
            {"error": "Please provide ('bot_id'), or ('channel_ids' and 'scope') in the JSON request body."}), 400

    bot_id = str(channel_ids[0])  # 문자열로 변환해서 조회
    logger.debug(f"Checking database for bot_id: {bot_id}")

    # MongoDB에서 해당 bot_id의 데이터를 조회
    bot_data = chatbot_collection.find_one({"chats.{}".format(bot_id): {"$exists": True}})

    if not bot_data:
        logger.error(f"MongoDB에 bot_id {bot_id}에 대한 데이터가 없습니다.")
        return jsonify({"error": f"MongoDB에 bot_id {bot_id}에 대한 데이터가 없습니다."}), 500

    logger.info(f"MongoDB에서 {bot_id} 데이터를 찾았습니다: {bot_data}")

    bot_instance = Watson._instances.get(bot_id)
    if not bot_instance:
        logger.error(f"Watson instance for bot_id {bot_id} not found.")
        return jsonify({"error": f"Watson instance for bot_id {bot_id} not found."}), 500

    if action == "ask":
        question = data.get("question", "")
        if not question:
            return jsonify({"error": "Question is required for action 'ask'"}), 400

        response = bot_instance.generate_response(question)
        return jsonify({"response": response})

    elif action == "reset":
        response = bot_instance.reset_conversation()
        return jsonify({"response": response})

    return jsonify({"error": "Invalid action."}), 400
