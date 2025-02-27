from pymongo import MongoClient
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertTokenizer, BertModel
from bs4 import BeautifulSoup

# MongoDB 연결 설정
client = MongoClient("mongodb://localhost:27017/")  # MongoDB 주소와 포트
db = client['local']  # 데이터베이스 이름
collection = db['test']  # 기존 데이터가 저장된 컬렉션 이름

# KoBERT 모델과 토크나이저 불러오기
model_name = "monologg/kobert"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# HTML 문서 전처리 함수
def preprocess_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator=' ')  # HTML 태그 제거 후 텍스트 추출
    return text.strip()

# KoBERT를 사용해 문서 임베딩 생성 함수
def get_bert_embedding(text):
    tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
    with torch.no_grad():
        output = model(**tokens)
    embedding = output.last_hidden_state[:, 0, :].squeeze().tolist()  # [CLS] 토큰 벡터 사용
    return embedding

# 클러스터 대표 임베딩을 MongoDB에서 불러오기
def fetch_cluster_representatives(db):
    cluster_representatives = {}
    cluster_collections = [col for col in db.list_collection_names() if col.startswith("cluster_")]
    for collection_name in cluster_collections:
        collection = db[collection_name]
        # 각 클러스터에서 저장된 문서들의 평균 임베딩을 계산
        embeddings = list(collection.find({}, {"embedding": 1, "_id": 0}))
        if embeddings:
            avg_embedding = np.mean([doc['embedding'] for doc in embeddings], axis=0)
            cluster_representatives[collection_name] = avg_embedding
    return cluster_representatives

# 새로운 게시글을 클러스터링에 맞게 저장하는 함수
def classify_and_save_new_post(new_post_html, cluster_representatives, db, similarity_threshold=0.5):
    # 새로운 게시글 전처리 및 임베딩 생성
    new_post_text = preprocess_html(new_post_html)
    new_post_embedding = get_bert_embedding(new_post_text)

    # 클러스터 대표 임베딩과의 유사도 계산
    max_similarity = -1
    best_cluster = None
    for cluster_name, representative_embedding in cluster_representatives.items():
        similarity = cosine_similarity([new_post_embedding], [representative_embedding])[0, 0]
        if similarity > max_similarity:
            max_similarity = similarity
            best_cluster = cluster_name

    # 임계값 이상일 경우 해당 클러스터에 저장, 아니면 노이즈 처리
    if max_similarity >= similarity_threshold and best_cluster:
        target_collection = db[best_cluster]
        target_collection.insert_one({"html_content": new_post_html, "embedding": new_post_embedding})
        print(f"New post saved to {best_cluster} (similarity: {max_similarity:.2f})")
    else:
        noise_collection = db["noise"]
        noise_collection.insert_one({"html_content": new_post_html, "embedding": new_post_embedding})
        print(f"New post saved to noise (similarity: {max_similarity:.2f})")

# 실행 예시
if __name__ == "__main__":
    # 1. 클러스터 대표 임베딩 불러오기
    cluster_representatives = fetch_cluster_representatives(db)

    # 2. 새로운 게시글 처리 및 저장
    new_post_html = "<html>새로운 게시글의 HTML 내용</html>"  # 새로운 게시글
    classify_and_save_new_post(new_post_html, cluster_representatives, db)
