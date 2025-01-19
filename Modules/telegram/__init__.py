from flask import Blueprint, request, jsonify

from .Telerecon import channelscraper, monitor
from .Telerecon.monitor import monitor_channel
from server.logger import logger

telegram_bp = Blueprint('telegram', __name__, url_prefix='/telegram')

@telegram_bp.route('/channel/scrape', methods=['POST'])
def scrape_channel():
    data = request.json
    if not data or 'channel_name' not in data:
        return jsonify({"error": "Please provide 'channel_name' in the JSON request body."}), 400

    channel_name = data['channel_name']
    logger.info("텔레그램 채널 스크랩 API 호출.")
    try:
        content = channelscraper.scrape(channel_name)
        return jsonify(content), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({"error": str(e)}), 500

@telegram_bp.route('/channel/check-suspicious', methods=['POST'])
def check_channel():
    data = request.json
    if not data or 'channel_name' not in data:
        return jsonify({"error": "Please provide 'channel_name' in the JSON request body."}), 400

    channel_name = data['channel_name']
    check_result = channelscraper.check(channel_name)
    try:
        return jsonify({"suspicious": check_result}), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({"error": str(e)}), 500

@telegram_bp.route('/channel/monitoring', methods=['POST'])
def monitor_channel():
    data = request.json
    if not data or 'channel_name' not in data:
        return jsonify({"error": "Please provide 'channel_name' in the JSON request body."}), 400
    elif 'how' not in data:
        return jsonify({"error": "Please provide 'how' in the JSON request body."}), 400

    try:
        channel_name = data['channel_name']
        how = data['how']
        if how == "start":
            monitor.start_monitoring(channel_name)
        elif how == "stop":
            monitor.stop_monitoring(channel_name)
        else:
            return jsonify({"error": "Invalid 'how'."}), 400

        return jsonify({"success": True}), 200
    except Exception as e:
        logger.error(str(e))
        return jsonify({"error": str(e)}), 500