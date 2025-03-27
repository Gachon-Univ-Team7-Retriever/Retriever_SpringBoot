from bs4 import BeautifulSoup

html_file_path = "sample_webpage.html"

with open(html_file_path, "r", encoding="utf-8") as file:
    html = file.read()  # 파일 내용을 문자열로 읽음

soup = BeautifulSoup(html, "html.parser")

# HTML 문서에서 텍스트 블록 추출
text_blocks = soup.get_text(separator=" ").split("\n")
text_blocks = [block.strip() for block in text_blocks if block.strip()]  # 빈 줄 제거

print(text_blocks)

from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

candidate_labels = ["광고글 제목", "광고글 내용", "기타"]
results = [classifier(block, candidate_labels) for block in text_blocks]

# 가장 높은 점수를 가진 라벨로 블록 분류
classified_blocks = [
    (block, result['labels'][0]) for block, result in zip(text_blocks, results)
]
for block, label in classified_blocks:
    print(f"[{label}] {block}")