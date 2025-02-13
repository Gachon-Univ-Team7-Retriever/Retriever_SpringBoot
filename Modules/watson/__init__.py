from flask import Blueprint, request, jsonify

from server.logger import logger
from telegram.Telegrasper.channel import is_channel_empty
from .watson import Watson
from utils import confirm_request

watson_bp = Blueprint('watson', __name__, url_prefix='/watson')

@watson_bp.route('/c', methods=['POST'])
def ask_watson():
    logger.info("챗봇 질문 API 호출됨.")
    data = request.json
    if response_for_invalid_request := confirm_request(data, ['question']):
        return response_for_invalid_request
    try:
        bot_id, channel_ids, scope = data.get('bot_id'), data.get('channel_ids'), data.get('scope')
        if bot_id and not isinstance(bot_id, int):
            return jsonify({"error": f"Please provide valid 'bot_id'. Expected type is integer, got {type(bot_id)}"}), 400
        if channel_ids and not isinstance(channel_ids, list):
            return jsonify({"error": f"Please provide valid 'channel_ids'. Expected type is list, got {type(channel_ids)}"}), 400
        if scope and scope not in (available_scopes := ["global", "local"]):
            return jsonify({"error": f"Please provide valid 'scope'. Valid values: {available_scopes}, got {scope}"}), 400
    except Exception as e:
        logger.error(str(e))
        return jsonify({"error": str(e)}), 500

    try:
        return jsonify({"answer": Watson(bot_id=bot_id, channel_ids=channel_ids, scope=scope).ask(data['question'])}), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({"error": str(e)}), 500
