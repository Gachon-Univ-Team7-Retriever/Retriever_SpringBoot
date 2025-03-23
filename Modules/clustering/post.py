from pymongo import MongoClient
import torch
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from transformers import BertTokenizer, BertModel
from bs4 import BeautifulSoup
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# MongoDB 연결 설정
client = MongoClient("mongodb://localhost:27017/")
db = client['local']
collection = db['train']
cluster_collection = db['post_clusters']  # 클러스터링 결과 저장 컬렉션

# KoBERT 모델 및 토크나이저 로드
model_name = "monologg/kobert"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# HTML 문서 불러오기
def fetch_html_documents():
    documents = collection.find({}, {"_id": 1, "html": 1})
    return [{"_id": str(doc["_id"]), "html": doc["html"]} for doc in documents if "html" in doc]

# HTML 전처리
def preprocess_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator=' ').strip()

# KoBERT 임베딩 생성
def get_bert_embedding(text):
    tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
    with torch.no_grad():
        output = model(**tokens)
    return output.last_hidden_state[:, 0, :].squeeze().tolist()

# 문체 분석 특징 추출
def extract_text_features(text):
    words = text.split()
    return [
        len(text),  # 전체 길이
        len(words),  # 단어 개수
        sum(len(w) for w in words) / len(words) if words else 0,  # 평균 단어 길이
        text.count(".") / len(words) if words else 0  # 문장 당 마침표 개수
    ]

# LDA 토픽 모델링 적용
def perform_lda(documents):
    vectorizer = CountVectorizer(stop_words="english", max_features=1000)
    X = vectorizer.fit_transform([doc["html"] for doc in documents])
    lda = LatentDirichletAllocation(n_components=10, random_state=42)
    lda_topic_vectors = lda.fit_transform(X)  # 학습하고 변환
    return lda_topic_vectors

# DBSCAN 클러스터링
def dbscan_clustering(similarity_matrix, eps, min_samples):
    scaler = MinMaxScaler()
    distance_matrix = scaler.fit_transform(1 - similarity_matrix)
    db = DBSCAN(metric="precomputed", eps=eps, min_samples=min_samples)
    return db.fit_predict(distance_matrix)

# 결합된 특징 벡터 생성 함수 (가중치 적용)
def combine_features_with_weights(embedding, text_feature, lda_topic_vector, embedding_weight=0.6, text_feature_weight=0.3, lda_weight=0.1):
    # 각 특징 벡터에 가중치를 적용하고 합침
    weighted_embedding = np.array(embedding) * embedding_weight
    weighted_text_feature = np.array(text_feature) * text_feature_weight
    weighted_lda_topic_vector = np.array(lda_topic_vector) * lda_weight

    # 가중치를 적용한 벡터 결합
    return np.concatenate([weighted_embedding, weighted_text_feature, weighted_lda_topic_vector])

# 클러스터링 실행 및 MongoDB 저장
def perform_clustering_with_features(eps=0.4, min_samples=2):
    documents = fetch_html_documents()

    embeddings = [get_bert_embedding(preprocess_html(doc["html"])) for doc in documents]

    # 문체 분석 특징 추출
    text_features = [extract_text_features(preprocess_html(doc["html"])) for doc in documents]

    # LDA 토픽 모델링 벡터 추출
    lda_topic_vectors = perform_lda(documents)

    # 각 문서에 대한 특성 벡터 결합
    feature_vectors = [
        combine_features_with_weights(embedding, text_feature, lda_topic_vector)
        for embedding, text_feature, lda_topic_vector in zip(embeddings, text_features, lda_topic_vectors)
    ]

    similarity_matrix = cosine_similarity(feature_vectors)

    # DBSCAN 클러스터링
    labels = dbscan_clustering(similarity_matrix, eps, min_samples)

    # 클러스터링 결과를 MongoDB에 저장
    cluster_collection.delete_many({})  # 기존 데이터 초기화

    for idx, doc in enumerate(documents):
        cluster_collection.insert_one({
            "_id": doc["_id"],
            "cluster_label": int(labels[idx]),
            "embedding": embeddings[idx],
            "text_features": text_features[idx],
            "lda_topic_vector": lda_topic_vectors[idx].tolist()
        })

    # 클러스터 통계 정보 저장
    cluster_collection.insert_one({
        "_id": "cluster_stats",
        "total_documents": len(documents),
        "noise_documents": list(labels).count(-1)
    })

    return {"message": "Clustering results stored successfully in MongoDB."}

