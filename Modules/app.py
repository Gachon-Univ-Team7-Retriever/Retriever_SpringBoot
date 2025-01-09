from flask import Flask, request, jsonify

from crawl import crawl_bp
from preprocess import preprocess_bp
from telegram import telegram_bp

import os
import sys

# 현재 app.py 파일의 디렉토리 경로를 sys.path에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)


app = Flask(__name__)

# 모든 Blueprint 등록
app.register_blueprint(crawl_bp)
app.register_blueprint(telegram_bp)
app.register_blueprint(preprocess_bp)


if __name__ == "__main__":
    print("Currently registered routes:")
    for rule in app.url_map.iter_rules():
        print(f"Route: {rule}, Methods: {rule.methods}, Endpoint: {rule.endpoint}")
    app.run(host="0.0.0.0", port=5000, debug=True)