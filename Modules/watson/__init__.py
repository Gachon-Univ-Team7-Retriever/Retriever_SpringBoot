from flask import Blueprint, request, jsonify

from server.logger import logger
from telegram.Telegrasper.channel import is_channel_empty
from .watson import Watson
from utils import confirm_request

watson_bp = Blueprint('watson', __name__, url_prefix='/watson')

@watson_bp.route('/c/<int:channel_id>', methods=['POST'])
def ask_watson(channel_id:int):
    logger.info("챗봇 질문 API 호출됨.")
    data = request.json
    if response_for_invalid_request := confirm_request(data, ['question']):
        return response_for_invalid_request

    if is_channel_empty(channel_id):
        return jsonify({"answer": Watson.error_msg_for_empty_data}), 200
    try:
        return jsonify({"answer": Watson(channel_id).ask(data['question'])}), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({"error": str(e)}), 500
