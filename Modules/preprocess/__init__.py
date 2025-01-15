from flask import Blueprint, request, jsonify

from . import extractor

preprocess_bp = Blueprint('preprocess', __name__, url_prefix='/preprocess')

# 수집한 웹 홍보글 HTML에서 홍보글의 내용 부분을 추출하는 API
@preprocess_bp.route("/extract/web-promotion", methods=["POST"])
def extract_text_block():
    try:
        # 요청에서 HTML 텍스트 가져오기
        html = request.get_json().get("html", "")
        if html is None:
            return jsonify({"error": "No HTML content provided"}), 400

        # HTML에서 텍스트 블록 추출
        result = extractor.extract_promotion_content(html)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500