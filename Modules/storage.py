from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import preprocess.extractor
import time
import os
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


# 검색 결과에서 URL을 가져오는 함수
def get_search_result(driver, query, max_results=42) -> dict:
    search_url = "https://www.google.com"
    driver.get(search_url)

    # 검색창에 검색어 입력
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)  # 검색 결과 로딩 대기

    urls = []
    telegrams = []

    while len(urls) < max_results:
        # 현재 페이지에서 URL 수집
        result_links = driver.find_elements(By.CSS_SELECTOR, "a")
        for link in result_links:
            href = link.get_attribute("href")
            print(href)
            if href:
                extract_result = preprocess.extractor.extract_telegram_links(href)
                if extract_result:
                    channel_name = extract_result[0].lower()
                    telegrams.append(channel_name)
                elif href and "http" in href and "google.com" not in href:
                    urls.append(href)
            if len(urls) >= max_results:
                break

        # 다음 페이지 버튼 클릭
        try:
            next_button = driver.find_element(By.ID, "pnnext")
            ActionChains(driver).move_to_element(next_button).click().perform()
            time.sleep(5)  # 다음 페이지 로딩 대기
        except Exception as e:
            print("다음 페이지가 없습니다.")
            break

    return {
        "urls": urls,
        "telegrams": telegrams
    }


def get_html_from_url(url: str) -> str:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_text = response.text
        return html_text
    except requests.RequestException as e:
        print(f"URL 요청 실패 ({url}): {e}")
        return ""


# 각 URL의 HTML 저장 함수
def save_html(html: str, folder_path: str, file_name: str) -> None:
    # 폴더가 없으면 생성
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html)
    print(f"{file_name} 저장 완료!")


# 메인 흐름 제어
def main(queries: list[str], max_results: int,
         save_file: bool = False) -> dict:  # 만약 로컬 파일에 결과를 저장하고 싶다면 save_file을 True로 변경
    # 중복 제거를 위한 집합 사용
    all_urls, all_telegrams = set(), set()

    # 드라이버 생성
    driver = webdriver.Chrome()

    # 반환할 결과 배열
    result = {
        'google': [],
        'telegrams': []
    }

    # 모든 검색어에 대한 검색 수행
    try:
        for query in queries:
            print(f"\n'{query}'에 대한 검색 시작...")
            search_result = get_search_result(driver, query, max_results)
            all_urls.update(search_result['urls'])  # URL 합집합
            all_telegrams.update(search_result['telegrams'])  # 텔레그램 채널 이름 합집합

    finally:
        driver.quit()

    if not all_urls:
        print("검색 결과가 없습니다.")
    else:
        print(f"{len(all_urls)}개의 URL을 찾았습니다.")

    # 검색한 결과를 json 형식으로 정리해서 반환
    for idx, url in enumerate(all_urls, start=1):
        html = get_html_from_url(url)

        print(f"url:{url}에 대한 결과 수신.")
        result['google'].append({
            "url": url,
            "html": html,
        })

        # save_file=True라면 로컬 파일에 검색 결과 html 저장
        if save_file:
            file_name = f"web_{idx}.html"
            save_html(html, "html_files", file_name)
        time.sleep(2)  # 요청 간격 조정

    # 텔레그램 채널 결과도 함께 반환
    result['telegrams'] = list(all_telegrams)

    return result

# 원래 channelscraper.py에 있던 기능
# from colorama import Fore, Style
# import pandas as pd
#
# async def main():
#     try:
#         channel_name = input(
#             f"{Fore.CYAN}Please enter a target Telegram channel (e.g., https://t.me/{Fore.LIGHTYELLOW_EX}your_channel{Style.RESET_ALL}):\n")
#         print(f'You entered "{Fore.LIGHTYELLOW_EX}{channel_name}{Style.RESET_ALL}"')
#         answer = input('Is this correct? (y/n)')
#         if answer != 'y':
#             return
#
#         output_directory = sanitizer.sanitize_filename(f"Collection/{channel_name}")
#         if not os.path.exists(output_directory):
#             os.makedirs(output_directory)
#
#         csv_filename = sanitizer.sanitize_filename(f'{output_directory}/{channel_name}_messages.csv')
#         print(f'Scraping content from {Fore.LIGHTYELLOW_EX}{channel_name}{Style.RESET_ALL}...')
#
#         content = await scrape_channel_content(channel_name)
#
#         if content:
#             df = pd.DataFrame(content, columns=['Datetime', 'Text', 'Username', 'First Name', 'Last Name', 'User ID', 'Views',
#                                                 'Message URL', 'Media File Path'])
#             try:
#                 df.to_csv(csv_filename, index=False)
#                 print(
#                     f'Successfully scraped and saved content to {Fore.LIGHTYELLOW_EX}{csv_filename}{Style.RESET_ALL}.')
#             except Exception as e:
#                 print(f"An error occurred while saving to CSV: {Fore.RED}{e}{Style.RESET_ALL}")
#         else:
#             print(f'{Fore.RED}No content scraped.{Style.RESET_ALL}')
#
#     except Exception as e:
#         print(f"An error occurred: {Fore.RED}{e}{Style.RESET_ALL}")
