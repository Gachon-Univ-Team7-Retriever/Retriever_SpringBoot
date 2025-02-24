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

# 현재 작업 디렉토리 (실행 시, 커맨드라인에서 지정된 디렉토리)
current_working_directory = os.getcwd()
# 경로 비교 시 경로 형식을 통일하기 위해 normpath()를 사용
if os.path.normpath(current_working_directory) != os.path.normpath(current_dir):
    raise Exception(f"현재 작업 디렉토리({current_working_directory})가 기대하는 디렉토리({current_dir})가 아닙니다.")

from server.logger import logger
app = Flask(__name__)
# 모든 Blueprint 등록
from crawl import crawl_bp
app.register_blueprint(crawl_bp)
from preprocess import preprocess_bp
app.register_blueprint(preprocess_bp)
from telegram import telegram_bp
app.register_blueprint(telegram_bp)
from watson import watson_bp
app.register_blueprint(watson_bp)


if __name__ == "__main__":
    logger.debug("Currently registered routes:")
    for rule in app.url_map.iter_rules():
        logger.debug(f"Route: {rule}, Methods: {rule.methods}, Endpoint: {rule.endpoint}")
    logger.info("Flask server has started!")
    app.run(host="0.0.0.0", port=5000)