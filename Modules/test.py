import requests


def google_search(query, api_key, search_engine_id, num_results=10):
    url = "https://www.googleapis.com/customsearch/v1"
    results = []
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "num": min(num_results, 10),  # 최대 10개까지 가능
        "start": 1  # 검색 시작 위치
    }

    while len(results) < num_results:
        response = requests.get(url, params=params)
        data = response.json()

        if "items" not in data:
            break

        for item in data["items"]:
            results.append(item["link"])  # 검색 결과 링크 저장
            if len(results) >= num_results:
                break

        params["start"] += 10  # 다음 페이지로 이동

    return results


# API 키와 검색 엔진 ID 설정
API_KEY = "AIzaSyBm9zsHc_L7SRJG9oLLWTAKxo03mjx3NC0"
SEARCH_ENGINE_ID = "36a59eacfc75c4fca"

# 검색 실행
query = "Python tutorial"
num_results = 20
search_results = google_search(query, API_KEY, SEARCH_ENGINE_ID, num_results)

# 검색 결과 출력
for idx, link in enumerate(search_results, 1):
    print(f"{idx}: {link}")

