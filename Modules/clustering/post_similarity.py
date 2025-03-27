
from pymongo import MongoClient
from transformers import BertTokenizer, BertModel
from bs4 import BeautifulSoup
from sklearn.metrics.pairwise import cosine_similarity
import torch

# MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")
db = client['local']
collection = db['test']
similarity_collection = db['post_similarity']

# KoBERT 모델 및 토크나이저 로드
model_name = "monologg/kobert"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# HTML 문서 불러오기
def fetch_html_documents():
    documents = list(collection.find({}, {"_id": 0, "html": 1}))
    return documents

# HTML 전처리
def preprocess_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator=' ').strip()

# KoBERT 임베딩 생성
def get_bert_embedding(text):
    tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
    with torch.no_grad():
        output = model(**tokens)
    return output.last_hidden_state[:, 0, :].squeeze().numpy()

# 유사도 분석 및 저장
def calculate_and_store_similarity():
    documents = fetch_html_documents()
    texts = [preprocess_html(doc['html']) for doc in documents]
    embeddings = [get_bert_embedding(text) for text in texts]

    # 코사인 유사도 계산
    similarity_matrix = cosine_similarity(embeddings)

    # 유사도 결과 MongoDB에 저장
    for idx, doc in enumerate(documents):
        base_doc = f"Document_{idx+1}"
        similarities = []
        for jdx, score in enumerate(similarity_matrix[idx]):
            if idx != jdx:
                target_doc = f"Document_{jdx+1}"
                similarities.append({"target_document": target_doc, "similarity": float(score)})

        # MongoDB에 저장
        similarity_collection.insert_one({
            "base_document": base_doc,
            "similarities": similarities
        })

    return {"message": "Similarity calculations stored successfully."}
# from pymongo import MongoClient
# from transformers import BertTokenizer, BertModel
# from bs4 import BeautifulSoup
# from sklearn.metrics.pairwise import cosine_similarity
# import torch
# import networkx as nx
# import community as community_louvain
#
# # MongoDB 연결
# client = MongoClient("mongodb://localhost:27017/")
# db = client['local']
# collection = db['test']
# similarity_collection = db['post_similarity']
#
# # KoBERT 모델 및 토크나이저 로드
# model_name = "monologg/kobert"
# tokenizer = BertTokenizer.from_pretrained(model_name)
# model = BertModel.from_pretrained(model_name)
#
# # HTML 문서 불러오기
# def fetch_html_documents():
#     documents = list(collection.find({}, {"_id": 0, "html": 1}))
#     return documents
#
# # HTML 전처리
# def preprocess_html(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     return soup.get_text(separator=' ').strip()
#
# # KoBERT 임베딩 생성
# def get_bert_embedding(text):
#     tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
#     with torch.no_grad():
#         output = model(**tokens)
#     return output.last_hidden_state[:, 0, :].squeeze().numpy()
#
# # 유사도 계산 후 그래프 생성
# def create_similarity_graph(similarity_matrix, threshold=0.5):
#     G = nx.Graph()
#     num_documents = len(similarity_matrix)
#
#     # 노드 추가
#     for i in range(num_documents):
#         G.add_node(i)
#
#     # 간선 추가 (유사도 점수가 threshold 이상일 경우)
#     for i in range(num_documents):
#         for j in range(i+1, num_documents):
#             if similarity_matrix[i][j] >= threshold:
#                 G.add_edge(i, j, weight=similarity_matrix[i][j])
#
#     return G
#
# # Louvain 방법 적용하여 커뮤니티 탐지
# def apply_louvain_community_detection(similarity_matrix):
#     G = create_similarity_graph(similarity_matrix)
#
#     # Louvain 알고리즘을 사용하여 커뮤니티 탐지
#     partition = community_louvain.best_partition(G)
#
#     return partition
#
# # 유사도 분석 및 Louvain 커뮤니티 탐지
# def calculate_and_store_similarity_with_louvain():
#     documents = fetch_html_documents()
#     texts = [preprocess_html(doc['html']) for doc in documents]
#     embeddings = [get_bert_embedding(text) for text in texts]
#
#     # 코사인 유사도 계산
#     similarity_matrix = cosine_similarity(embeddings)
#
#     # Louvain 방법 적용하여 커뮤니티 탐지
#     partition = apply_louvain_community_detection(similarity_matrix)
#
#     # 커뮤니티 결과 출력
#     for community, docs in partition.items():
#         print(f"Community {community}: {docs}")
#
#     # 유사도 결과 MongoDB에 저장
#     for idx, doc in enumerate(documents):
#         base_doc = f"Document_{idx+1}"
#         similarities = []
#         for jdx, score in enumerate(similarity_matrix[idx]):
#             if idx != jdx:
#                 target_doc = f"Document_{jdx+1}"
#                 similarities.append({"target_document": target_doc, "similarity": float(score)})
#
#         # MongoDB에 저장
#         similarity_collection.insert_one({
#             "base_document": base_doc,
#             "similarities": similarities,
#             "community": partition[idx]  # 커뮤니티 정보 추가
#         })
#
#     return {"message": "Similarity calculations and community detection stored successfully."}
#
# # 실행
# calculate_and_store_similarity_with_louvain()
