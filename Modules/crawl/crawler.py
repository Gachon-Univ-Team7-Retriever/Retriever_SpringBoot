from preprocess import extractor
import os
import requests
from server.logger import logger

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# API 키와 검색 엔진 ID 설정
API_KEY = "AIzaSyASbWkCO8xFGSzYT44Xq4HHqZyE1Zv84Dk"
SEARCH_ENGINE_ID = "369613352bc34466e"

# 구글 검색 결과에서 URL을 가져오는 함수
def google_search(query:str, num_results:int=10, api_key:str=API_KEY, search_engine_id:str=SEARCH_ENGINE_ID) -> dict[str:list, str:list]:
    url = "https://www.googleapis.com/customsearch/v1"
    urls, telegrams = [], []
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "gl": "kr", # 지역을 한국으로 설정 (검색 결과 향상을 목표로 했으나 달라지는 게 없어 보임)
        "hl": "ko", # 지역을 한국으로 설정 (검색 결과 향상을 목표로 했으나 달라지는 게 없어 보임)
        "num": min(num_results, 10),  # 최대 10개까지 가능
        "start": 1  # 검색 시작 위치
    }

    while len(urls) + len(telegrams) < num_results:
        # 검색을 수행하고 결과를 수신
        response = requests.get(url, params=params)
        data = response.json()

        # 검색 결과가 없을 경우(검색 결과의 끝에 도달했을 경우) 검색 중단
        if "items" not in data:
            break
        
        # 검색 결과가 있을 경우 검색 결과로 나온 링크를 순회
        for item in data["items"]:
            link = item["link"]
            extracted_telegram_links = extractor.extract_telegram_links(link)
            # 추출된 텔레그램 링크가 있을 경우 텔레그램 항목에 추가
            # Google 검색 결과이기 때문에 반환된 텔레그램 주소 목록은 1개뿐이고, 때문에 index=0만 바로 사용
            if extracted_telegram_links:
                channel_name = extracted_telegram_links[0].lower()
                telegrams.append(channel_name)
            else:
                urls.append(link)  # 검색 결과 링크 저장
            if len(urls) + len(telegrams) >= num_results:
                break

        params["start"] += 10  # 다음 페이지로 이동

    return urls, telegrams


# 통합 웹 검색
from utils import merge_lists_remove_duplicates
def search_links(queries: list[str], max_results: int) -> dict:  # 만약 로컬 파일에 결과를 저장하고 싶다면 save_file을 True로 변경
    logger.info(f'검색어 {len(queries)}개에 대한 검색 시작...')
    # 모든 검색어에 대한 검색 수행
    all_urls, all_telegrams = {}, {}
    for query in queries:
        logger.debug(f'검색어 "{query}"에 대한 검색 시작...')
        # 검색 후 값 저장
        urls, telegrams = google_search(query, max_results)
        all_urls[query], all_telegrams[query] = urls, telegrams
        logger.debug(f'검색어 "{query}"에 대한 검색 결과: URL {len(urls)}개, Telegram 채널 {len(telegrams)}개')

    all_urls, all_telegrams = merge_lists_remove_duplicates(all_urls.values()), merge_lists_remove_duplicates(all_telegrams.values())

    if not all_urls:
        logger.info(f"검색어 {len(queries)}개에 대한 전체 검색 결과가 없습니다.")
    else:
        logger.info(f"검색어 {len(queries)}개에 대한 검색 결과: URL {len(all_urls)}개, Telegram 채널 {len(all_telegrams)}")

    # URL들과 텔레그램 채널 결과를 합쳐서 딕셔너리로 결과 반환
    return {
        'google': list(all_urls),
        'telegrams': list(all_telegrams)
    }


def get_html_from_url(url: str) -> str:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_text = response.text
        return html_text
    except requests.RequestException as e:
        logger.warning(f"URL [{url}] 에 대한 요청 실패: {e}")
        return ""

# 각 URL의 HTML 저장 함수(현재 미사용)
def save_html(html:str, folder_path:str, file_name:str) -> None:
    # 폴더가 없으면 생성
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html)
    logger.info(f"HTML 다음 경로에 저장함: {file_name}")
