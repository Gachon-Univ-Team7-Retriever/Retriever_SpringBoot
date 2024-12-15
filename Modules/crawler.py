from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import requests

# 검색 결과에서 URL을 가져오는 함수
def get_search_result_urls(driver, query, max_results=42):
    search_url = "https://www.google.com"
    driver.get(search_url)

    # 검색창에 검색어 입력
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)  # 검색 결과 로딩 대기

    urls = []

    while len(urls) < max_results:
        # 현재 페이지에서 URL 수집
        result_links = driver.find_elements(By.CSS_SELECTOR, "a")
        for link in result_links:
            href = link.get_attribute("href")
            if href and "http" in href and "google.com" not in href:
                urls.append(href)
                if len(urls) >= max_results:
                    break

        # 다음 페이지 버튼 클릭
        try:
            next_button = driver.find_element(By.ID, "pnnext")
            ActionChains(driver).move_to_element(next_button).click().perform()
            time.sleep(2)  # 다음 페이지 로딩 대기
        except Exception as e:
            print("다음 페이지가 없습니다.")
            break

    return urls

def get_html_from_url(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_text = response.text
        return html_text
    except requests.RequestException as e:
        print(f"URL 요청 실패 ({url}): {e}")
        return ""

# 각 URL의 HTML 저장 함수
def save_html(html:str, folder_path:str, file_name:str) -> None:
    # 폴더가 없으면 생성
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html)
    print(f"{file_name} 저장 완료!")

# 메인 흐름 제어
def main(query, save_file=False) -> list:
    # 드라이버 생성
    driver = webdriver.Chrome()

    # 반환할 결과 배열
    result = []

    try:
        urls = get_search_result_urls(driver, query, max_results=10)
    finally:
        driver.quit()

    if not urls:
        print("검색 결과가 없습니다.")
    else:
        print(f"{len(urls)}개의 URL을 찾았습니다.")

    for idx, url in enumerate(urls, start=1):
        html = get_html_from_url(url)

        print(f"url:{url}에 대한 결과 수신.")
        result.append({
            "url": url,
            "html": html,
        })
        if save_file:
            file_name = f"web_{idx}.html"
            save_html(html, "html_files", file_name)
        time.sleep(2)  # 요청 간격 조정

    return result

# 프로그램 실행
if __name__ == "__main__":
    main()
