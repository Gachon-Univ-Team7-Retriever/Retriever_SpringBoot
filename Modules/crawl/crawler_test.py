import requests
import json

if __name__ == '__main__':
    test_result = {
        'urls': [],
        'telegrams': []
    }

    response = requests.post("http://127.0.0.1:5000/crawl/google", json={
        "queries": [
            "t.me 아이스",
            "t.me 떨",
            "t.me 캔디",
            "t.me LSD",
            "t.me 케타민",
            "텔레 떨 판매",
            "텔레 아이스 판매",
        ],
        "max_results": 100
    })

    test_result['telegrams'] = response.json()['telegrams']

    for idx, url_and_html in enumerate(response.json()['google'], start=1):
        response = requests.post("http://127.0.0.1:5000/preprocess/extract/web_promotion", json={
            "html": url_and_html["html"]
        })
        extracted_content = response.json().get("promotion_content")
        test_result['urls'].append({
            "url": url_and_html['url'],
            "html_len": len(url_and_html["html"]),
            "extracted_content": extracted_content
        })
        if extracted_content:
            print(extracted_content)
        if idx % 10 == 0:
            print(f"URL의 HTML을 받아오는 중...({idx}/{len(response.json())})")

    json.dump(test_result, open("crawler_test_result.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)
