from bs4 import BeautifulSoup
import os

def extract_text_blocks_from_html(html) -> list:
    # HTML 문서에서 텍스트 블록 추출
    soup = BeautifulSoup(html, "html.parser")
    text_blocks = soup.get_text(separator=" ").split("\n")
    text_blocks = [block.strip() for block in text_blocks if block.strip()]  # 빈 줄 제거

    return text_blocks

import json

# 텍스트 길이가 가장 길고 특정 텍스트를 포함하는 원소를 반환하는 함수
def extract_by_length(strings) -> str | None:
    # json 파일에서 마약 은어/약어 로드(추후 데이터베이스에서 로드하도록 변경)
    # 모듈 기준으로 drug_dictionary.json 파일 경로 계산
    current_dir = os.path.dirname(__file__)  # 현재 파일(extractor.py)의 디렉토리
    dictionary_path = os.path.join(current_dir, "drug_dictionary.json")

    with open(dictionary_path, "r", encoding="utf-8") as filestream:
        dictionary = json.load(filestream)
        
    # 은어/약어 사전에맞는 문자열들을 필터링
    filtered_strings = [chunk for chunk in strings if any(keyword in chunk for keyword in dictionary)]

    # 조건에 맞는 문자열 중 가장 긴 문자열 반환
    if filtered_strings:
        return str(max(filtered_strings, key=len))

    return None

def extract_promotion_content(html: str) -> None | str:
    return extract_by_length(extract_text_blocks_from_html(html))


# html_file_path = "/sample_webpage.html"
#
# with open(html_file_path, "r", encoding="utf-8") as file:
#     sample_html = file.read()  # 파일 내용을 문자열로 읽음


# sample_text_blocks = extract_text_blocks_from_html(sample_html)
# print(sample_text_blocks)
# print(extract_by_length(sample_text_blocks))
