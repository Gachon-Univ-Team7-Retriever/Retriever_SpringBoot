from pymongo import MongoClient
from transformers import BertTokenizer, BertModel
from bs4 import BeautifulSoup
from sklearn.metrics.pairwise import cosine_similarity
import torch
import numpy as np
import networkx as nx
from community import community_louvain

# MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")
db = client['local']
collection = db['channels']
similarity_collection = db['channel_similarity']

# KoBERT 모델 및 토크나이저 로드
model_name = "monologg/kobert"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# 마약 키워드 가중치 설정
drug_keywords = {
    '코카인': 2.0,
    '메스암페타민': 2.0,
    '펜타닐': 2.5,
    'LSD': 1.8,
    '엑스터시': 2.0
}

# HTML 전처리 및 클린 텍스트 생성
def preprocess_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator=' ').strip()
    text = ' '.join(text.split())  # 중복 공백 제거
    return text

# 가중치 적용 텍스트 전처리 (단어 가중치 적용)
def apply_keyword_weight(text):
    words = text.split()
    weighted_words = []
    for word in words:
        weight = drug_keywords.get(word, 1.0)
        weighted_words.append((word + ' ') * int(weight))
    return ' '.join(weighted_words)

# KoBERT 임베딩 생성 (평균 풀링 적용)
def get_bert_embedding(text):
    tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
    with torch.no_grad():
        output = model(**tokens)
    embeddings = output.last_hidden_state.squeeze(0)
    return embeddings.mean(dim=0).numpy()  # 평균 풀링 적용

# 채널 유사도 분석 및 저장 (MongoDB 성능 최적화)
def calculate_and_store_similarity():
    documents = list(collection.find({}, {"_id": 1, "html": 1}))
    texts = [apply_keyword_weight(preprocess_html(doc['html'])) for doc in documents]
    embeddings = [get_bert_embedding(text) for text in texts]

    # 코사인 유사도 계산
    similarity_matrix = cosine_similarity(embeddings)

    # 그래프 생성 및 Louvain 커뮤니티 탐지
    G = nx.Graph()
    for idx, doc in enumerate(documents):
        G.add_node(doc['_id'], label=f"Channel_{idx+1}")
        for jdx, score in enumerate(similarity_matrix[idx]):
            if idx != jdx and score > 0.75:
                G.add_edge(doc['_id'], documents[jdx]['_id'], weight=score)

    # Louvain 알고리즘 적용 (resolution 파라미터 조정 가능)
    partition = community_louvain.best_partition(G, resolution=1.0)

    # 결과 저장 (insert_many로 성능 향상)
    similarity_data = [{"channel_id": node, "community": community} for node, community in partition.items()]
    if similarity_data:
        similarity_collection.insert_many(similarity_data)

    return {"message": "Channel similarity and communities stored successfully."}

# 실행
if __name__ == "__main__":
    try:
        result = calculate_and_store_similarity()
        print(result)
    except Exception as e:
        print(f"Error: {e}")
