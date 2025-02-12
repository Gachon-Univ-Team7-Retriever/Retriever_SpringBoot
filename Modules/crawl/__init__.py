from flask import Blueprint, request, jsonify
from utils import confirm_request
from . import crawler

crawl_bp = Blueprint('crawl', __name__, url_prefix='/crawl')
@crawl_bp.route('/links', methods=["POST"])
def crawl_web_links():
    data = request.json
    if response_for_invalid_request := confirm_request(data, ['queries', 'max_results']):
        return response_for_invalid_request

    try:
        result = crawler.search_links(data['queries'], data['max_results'])
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@crawl_bp.route('/html', methods=["POST"])
def link_to_html():
    data = request.json
    if not data or 'link' not in data:
        return jsonify({"error": "Please provide 'link' in the request arguments."}), 400

    try:
        result = crawler.get_html_from_url(data['link'])
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500