# from matplotlib import pyplot as plt
# from pymongo import MongoClient
# import torch
# import numpy as np
# from sklearn.cluster import DBSCAN
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.metrics import adjusted_rand_score
# from collections import Counter, defaultdict
# from scipy.optimize import linear_sum_assignment
# from sklearn.neighbors import NearestNeighbors
# from sklearn.preprocessing import MinMaxScaler
# from transformers import BertTokenizer, BertModel
# from bs4 import BeautifulSoup
#
# # MongoDB 연결 설정
# client = MongoClient("mongodb://localhost:27017/")
# db = client['local']
# collection = db['test']
#
# # MongoDB에서 HTML 문서 불러오기
# def fetch_html_documents():
#     documents = collection.find({}, {"_id": 0, "html": 1})
#     html_docs = [doc['html'] for doc in documents if 'html' in doc]
#     return html_docs
#
# # KoBERT 모델과 토크나이저 불러오기
# model_name = "monologg/kobert"
# tokenizer = BertTokenizer.from_pretrained(model_name)
# model = BertModel.from_pretrained(model_name)
#
# # HTML 문서 전처리 함수
# def preprocess_html(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     text = soup.get_text(separator=' ')
#     return text.strip()
#
# # KoBERT를 사용해 문서 임베딩 생성 함수
# def get_bert_embedding(text):
#     tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
#     with torch.no_grad():
#         output = model(**tokens)
#     embedding = output.last_hidden_state[:, 0, :].squeeze().tolist()
#     return embedding
#
# # DBSCAN 클러스터링 함수
# def dbscan_clustering(similarity_matrix, eps, min_samples):
#     scaler = MinMaxScaler()
#     distance_matrix = scaler.fit_transform(1 - similarity_matrix)
#     db = DBSCAN(metric="precomputed", eps=eps, min_samples=min_samples)
#     labels = db.fit_predict(distance_matrix)
#     return labels
#
# # 클러스터 매칭 후 정확도 평가
# def match_clusters(manual_labels, auto_labels):
#     unique_manual = np.unique(manual_labels)
#     unique_auto = np.unique(auto_labels)
#
#     cost_matrix = np.zeros((len(unique_manual), len(unique_auto)))
#     for i, m_label in enumerate(unique_manual):
#         for j, a_label in enumerate(unique_auto):
#             cost_matrix[i, j] = -np.sum((manual_labels == m_label) & (auto_labels == a_label))
#
#     row_ind, col_ind = linear_sum_assignment(cost_matrix)
#     mapping = {unique_auto[col]: unique_manual[row] for row, col in zip(row_ind, col_ind)}
#     return mapping
#
# # MongoDB에서 HTML 문서 불러오기
# html_documents = fetch_html_documents()
#
# # 유사도 행렬 계산
# similarity_matrix = cosine_similarity([get_bert_embedding(preprocess_html(doc)) for doc in html_documents])
#
# # DBSCAN 클러스터링 수행
# labels = dbscan_clustering(similarity_matrix, eps=0.4, min_samples=2)
#
# # 수동 클러스터링
# manual_labels = [0, 1, 2, 0, 1, 2]  # 메신저,sns는 클러스터 0, 다크웹 마켓는 클러스터 1, 후기 포함은 클러스터 2
#
# # Adjusted Rand Index (ARI) 평가
# ari_score = adjusted_rand_score(manual_labels, labels)
# print(f"Adjusted Rand Index (ARI): {ari_score:.4f}")
#
# # 클러스터 매칭 후 정확도 평가
# mapping = match_clusters(np.array(manual_labels), np.array(labels))
# mapped_auto_labels = np.array([mapping.get(label, -1) for label in labels])
# accuracy = np.mean(mapped_auto_labels == manual_labels)
# print(f"Clustering Accuracy: {accuracy:.4%}")
#
# # 클러스터 크기 비교
# manual_counts = Counter(manual_labels)
# auto_counts = Counter(labels)
# print("Manual Clustering Distribution:", manual_counts)
# print("Auto Clustering Distribution:", auto_counts)
#
# # # 클러스터별 대표 문서 출력
# # for cluster_id in set(labels):
# #     if cluster_id != -1:
# #         print(f"\n=== Auto Cluster {cluster_id} Example ===\n{html_documents[labels.tolist().index(cluster_id)][:500]}")
# #     if cluster_id in manual_labels:
# #         print(f"\n=== Manual Cluster {cluster_id} Example ===\n{html_documents[manual_labels.index(cluster_id)][:500]}")
#
# cluster_dict = defaultdict(list)
# for doc, label in zip(html_documents, labels):
#     cluster_dict[label].append(doc[:500])  # 긴 HTML은 500자까지만 표시
#
# for cluster_id, docs in cluster_dict.items():
#     print(f"\n=== Cluster {cluster_id} ({len(docs)} documents) ===\n")
#     for doc in docs:
#         print(doc)
#         print("-" * 80)  # 구분선
#
# # noise_docs = [html_documents[i] for i, label in enumerate(labels) if label == -1]
# # noise_embeddings = [get_bert_embedding(preprocess_html(doc)) for doc in noise_docs]
# # noise_similarity_matrix = cosine_similarity(noise_embeddings)
# #
# # print("\n🚨 노이즈 문서 간 유사도 행렬 🚨")
# # print(noise_similarity_matrix)
#
# # # k-NN으로 거리 계산 (k=2)
# # neighbors = NearestNeighbors(n_neighbors=2, metric="precomputed")
# # neighbors_fit = neighbors.fit(1 - similarity_matrix)
# # distances, _ = neighbors_fit.kneighbors(1 - similarity_matrix)
# #
# # # 거리 값 정렬 후 그래프 출력
# # distances = np.sort(distances[:, 1], axis=0)
# # plt.plot(distances)
# # plt.xlabel("Points sorted by distance")
# # plt.ylabel("2nd Nearest Neighbor Distance")
# # plt.title("Finding optimal eps for DBSCAN")
# # plt.show()

from pymongo import MongoClient
import torch
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
from sklearn.preprocessing import MinMaxScaler
from transformers import BertTokenizer, BertModel
from bs4 import BeautifulSoup

# MongoDB 연결 설정
client = MongoClient("mongodb://localhost:27017/")
db = client['local']
collection = db['test']
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

# DBSCAN 클러스터링
def dbscan_clustering(similarity_matrix, eps, min_samples):
    scaler = MinMaxScaler()
    distance_matrix = scaler.fit_transform(1 - similarity_matrix)
    db = DBSCAN(metric="precomputed", eps=eps, min_samples=min_samples)
    return db.fit_predict(distance_matrix)

# 클러스터링 실행 및 MongoDB 저장
def perform_clustering(eps=0.4, min_samples=2):
    documents = fetch_html_documents()
    embeddings = [get_bert_embedding(preprocess_html(doc["html"])) for doc in documents]
    similarity_matrix = cosine_similarity(embeddings)
    labels = dbscan_clustering(similarity_matrix, eps, min_samples)

    # 클러스터링 결과를 MongoDB에 저장
    cluster_collection.delete_many({})  # 기존 데이터 초기화

    for idx, doc in enumerate(documents):
        cluster_collection.insert_one({
            "_id": doc["_id"],
            "cluster_label": int(labels[idx]),
            "embedding": embeddings[idx]
        })

    # 클러스터 통계 정보 저장
    cluster_collection.insert_one({
        "_id": "cluster_stats",
        "total_documents": len(documents),
        "noise_documents": list(labels).count(-1)
    })

    return {"message": "Clustering results stored successfully in MongoDB."}


