import logging

from bs4 import BeautifulSoup
import os

from server.logger import logger
from typing import Optional, Union

def extract_text_blocks_from_html(html) -> list:
    # HTML 문서에서 텍스트 블록 추출
    soup = BeautifulSoup(html, "html.parser")
    text_blocks = soup.get_text(separator=" ").split("\n")
    text_blocks = [block.strip() for block in text_blocks if block.strip()]  # 빈 줄 제거

    return text_blocks


import json

# json 파일에서 마약 은어/약어 로드(추후 데이터베이스에서 로드하도록 변경)
# 모듈 기준으로 drug_dictionary.json 파일 경로 계산
current_dir = os.path.dirname(__file__)  # 현재 파일(extractor.py)의 디렉토리
dictionary_path = os.path.join(current_dir, "drug_dictionary.json")
with open(dictionary_path, "r", encoding="utf-8") as filestream:
    dictionary = json.load(filestream)

# 텍스트 길이가 가장 길고 특정 텍스트를 포함하는 원소를 반환하는 함수
def extract_by_length(strings: Union[str, list[str]]) -> Optional[str]:
    # 은어/약어 사전에 맞는 문자열들을 필터링
    filtered_strings = [chunk for chunk in strings if sum(keyword in chunk for keyword in dictionary) >= 3]

    # 조건에 맞는 문자열이 있다면 가장 긴 문자열을 글 내용으로 반환하고, 없다면 None 반환
    return str(max(filtered_strings, key=len)) if filtered_strings else None


# HTML 텍스트에서 마약 홍보에 관련된 유의미한 글 내용을 추출하고, 발견된 텔레그램 주소가 있다면 주소까지 반환하는 함수
def extract_promotion_content(html: str) -> dict[str, str]:
    # 전체 HTMl 텍스트를 블록으로 분할하여 유의미한 텍스트를 추출해보고, 없다면 None 저장
    logger.debug(f"HTML 텍스트에서 마약 홍보 관련 내용 추출 시작. 텍스트 길이: {len(html)}")
    extracted_content = extract_by_length(text_blocks := extract_text_blocks_from_html(html))
    # 추출된 결과가 있다면 텔레그램 주소도 찾아보고, 없다면 텔레그램 주소도 빈 배열로 반환
    telegrams = extract_telegram_links(text_blocks) if extracted_content else []

    logger.debug(f"HTML 텍스트에서 추출한 결과: * 유의미한 글 내용: "
                 f"{'있음, * 발견된 텔레그램 주소: '+str(len(telegrams))+'개' if extracted_content else '없음'}")
    return {
        "promotion_content": extracted_content,
        "telegrams": telegrams
    }


import re

# 텍스트에서 텔레그램 링크들을 식별해서 리스트로 묶어 반환하는 함수
def extract_telegram_links(data: Union[str, list[str]]) -> list[str]:
    # 텔레그램 주소를 식별하는 정규식 패턴
    telegram_pattern = r"(?:https?://)?t\.me/(?:s/|joinchat/)?([~+]?[a-zA-Z0-9_-]+)(?:/\d+)?"

    # 정규식으로 텔레그램 주소 추출
    if isinstance(data, str):
        return re.findall(telegram_pattern, data)
    elif isinstance(data, list):
        if all([isinstance(text, str) for text in data]):
            # 만약 data가 string의 list일 경우, list 안에 있는 text에 대해서 정규식으로 모두 찾은 다음 list를 flatten해서 반환
            return [telegram_link for regex_result in map(re.findall, [telegram_pattern]*len(data), data) for telegram_link in regex_result]
        else:
            logging.critical("Input data of function for extract_telegram_links should be a string or a list of string, "
                             "but found something else in the list.")
            return []
    else:
        logging.critical("Input data of function for extract_telegram_links should be a string or a list of string, "
                         f"got {type(data)}.")
        return []




if __name__ == "__main__":
    print(extract_telegram_links("http://t.me/+sample"))