from flask import Blueprint, request, jsonify

from utils import confirm_request
from .watson import Watson
from server.logger import logger

watson_bp = Blueprint('watson', __name__, url_prefix='/watson')

@watson_bp.route('/c', methods=['POST'])
def chat_with_watson():
    data = request.json
    # if response_for_invalid_request := confirm_request(data, {
    #     'action': (str, ["ask", "reset"]),
    #     'bot_id': typing.Optional[int],
    #     'channel_ids': typing.Optional[list],
    #     'scope': (typing.Optional[str], ["global", "local"])
    # }):
    #     return response_for_invalid_request
    if not data.get('bot_id') and (not data.get('scope') or not data.get('channel_ids')):
        return {"error": f"Please provide ('bot_id'), or ('channel_ids' and 'scope') in the JSON request body."}

    bot = Watson(
        bot_id=data.get('bot_id'),
        channel_ids=data.get('channel_ids'),
        scope=data.get('scope')
    )
    if data['action'] == "ask":
        return ask_watson(bot, data)
    elif data['action'] == "reset":
        bot.clear_message_history()
        return jsonify({"success": True}), 200


def ask_watson(bot, data):
    """챗봇에게 질문을 던지고 결과를 반환하는 함수."""
    try:
        if response_for_invalid_request := confirm_request(data, {
            'question': str,
        }):
            return response_for_invalid_request
        return jsonify({"answer": bot.ask(data['question'])}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({"answer": f"죄송합니다. 에러가 발생했습니다. 시스템, 또는 AI를 제공하는 외부 API의 문제일 수 있습니다."}), 500