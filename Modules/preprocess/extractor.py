from bs4 import BeautifulSoup
import os

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
def extract_by_length(strings) -> str | None:
    # 은어/약어 사전에 맞는 문자열들을 필터링
    filtered_strings = [chunk for chunk in strings if sum(keyword in chunk for keyword in dictionary) >= 3]

    # 조건에 맞는 문자열 중 가장 긴 문자열 반환
    if filtered_strings:
        return str(max(filtered_strings, key=len))
    # 조건에 맞는 문자열이 없을 경우 None 반환
    else:
        return None

def extract_promotion_content(html: str) -> None | str:
    return extract_by_length(extract_text_blocks_from_html(html))


import re

# 텍스트에서 텔레그램 링크들을 식별해서 리스트로 묶어 반환하는 함수
def extract_telegram_links(text: str) -> list[str]:
    # joinchat/를 "+"로 변환
    text_modified = re.sub(r"(https?://)?t\.me/joinchat/", r"\1t.me/+", text)
    # 텔레그램 주소를 식별하는 정규식 패턴
    telegram_pattern = r"(?:https?://)?t\.me/(?:s/|joinchat/)?([~+]?[a-zA-Z0-9_-]+)(?:/\d+)?"

    # 정규식으로 텔레그램 주소 추출
    return re.findall(telegram_pattern, text_modified)




if __name__ == "__main__":
    print(extract_telegram_links("http://t.me/+sample"))