from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import requests

# 검색 결과에서 URL을 가져오는 함수
def get_search_result_urls(driver, query, max_results=50):
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

# 각 URL의 HTML 저장 함수
def save_html_from_url(url, folder_path, file_name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_text = response.text

        # 폴더가 없으면 생성
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_text)
        print(f"{file_name} 저장 완료!")
    except requests.RequestException as e:
        print(f"URL 요청 실패 ({url}): {e}")

# 메인 흐름 제어
def main():
    query = input("검색어를 입력하세요: ")

    # 드라이버 생성
    driver = webdriver.Chrome()

    try:
        urls = get_search_result_urls(driver, query, max_results=50)

        if not urls:
            print("검색 결과가 없습니다.")
            return

        print(f"{len(urls)}개의 URL을 찾았습니다. HTML 파일 저장을 시작합니다...")

        folder_path = "html_files"
        for idx, url in enumerate(urls, start=1):
            file_name = f"web_{idx}.html"
            save_html_from_url(url, folder_path, file_name)
            time.sleep(2)  # 요청 간격 조정

        print("모든 HTML 파일 저장이 완료되었습니다!")
    finally:
        driver.quit()

# 프로그램 실행
if __name__ == "__main__":
    main()
