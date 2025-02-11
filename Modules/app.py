from flask import Flask, request, jsonify

import os
import sys
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 현재 app.py 파일의 디렉토리 경로를 sys.path에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# 현재 app.py 파일의 디렉토리의 부모 디렉토리 경로를 sys.path에 추가
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from crawl import crawl_bp
from preprocess import preprocess_bp
from telegram import telegram_bp

from server.logger import logger


app = Flask(__name__)

# 모든 Blueprint 등록
app.register_blueprint(crawl_bp)
app.register_blueprint(telegram_bp)
app.register_blueprint(preprocess_bp)


if __name__ == "__main__":
    logger.debug("Currently registered routes:")
    for rule in app.url_map.iter_rules():
        logger.debug(f"Route: {rule}, Methods: {rule.methods}, Endpoint: {rule.endpoint}")
    logger.info("Flask server has started!")
    app.run(host="0.0.0.0", port=5000, debug=True)