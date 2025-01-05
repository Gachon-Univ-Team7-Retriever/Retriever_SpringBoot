from flask import Flask, request, jsonify

import preprocessor.extractor
import Telerecon.channelscraper
import crawler

app = Flask(__name__)

# 수집한 웹 홍보글 HTML에서 홍보글의 내용 부분을 추출하는 코드
@app.route("/preprocess/extract/web_promotion", methods=["POST"])
def extract_text_block():
    try:
        # 요청에서 HTML 텍스트 가져오기
        html = request.get_json().get("html", "")

        if not html:
            return jsonify({"error": "No HTML content provided"}), 400

        # HTML에서 텍스트 블록 추출
        promotion_content = preprocessor.extractor.extract_promotion_content(html)

        return jsonify({
            "promotion_content": promotion_content
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/telegram/channel/scrape', methods=['POST'])
def scrape():
    data = request.json
    if not data or 'channel_name' not in data:
        return jsonify({"error": "Please provide 'channel_name' in the JSON request body."}), 400

    channel_name = data['channel_name']

    try:
        content = Telerecon.channelscraper.main(channel_name)
        return jsonify(content), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/crawl/google', methods=["POST"])
def crawl():
    data = request.json
    if not data or 'queries' not in data:
        return jsonify({"error": "Please provide 'queries' in the request arguments."}), 400
    if not data or 'max_results' not in data:
        return jsonify({"error": "Please provide 'max_results' in the request arguments."}), 400

    try:
        result = crawler.main(data['queries'], data['max_results'])
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)