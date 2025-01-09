from flask import Blueprint, request, jsonify

from .Telerecon import channelscraper

telegram_bp = Blueprint('telegram', __name__, url_prefix='/telegram')

@telegram_bp.route('/channel/scrape', methods=['POST'])
def scrape_channel():
    data = request.json
    if not data or 'channel_name' not in data:
        return jsonify({"error": "Please provide 'channel_name' in the JSON request body."}), 400

    channel_name = data['channel_name']

    try:
        content = channelscraper.scrape(channel_name)
        return jsonify(content), 200
    except Exception as e:
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
        return jsonify({"error": str(e)}), 500