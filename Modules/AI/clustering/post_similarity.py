# from pymongo import MongoClient
# from transformers import BertTokenizer, BertModel
# from bs4 import BeautifulSoup
# from sklearn.metrics.pairwise import cosine_similarity
# import torch
# import numpy as np
#
# # MongoDB 연결 설정
# client = MongoClient("mongodb://localhost:27017/")
# db = client['local']
# collection = db['test']
# similarity_collection = db['post_similarity']  # 새 컬렉션 생성
#
# # MongoDB에서 HTML 문서 불러오기
# def fetch_html_documents():
#     documents = list(collection.find({}, {"_id": 0, "html": 1}))
#     return documents
#
# # HTML 문서 전처리 함수
# def preprocess_html(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     text = soup.get_text(separator=' ')
#     return text.strip()
#
# # KoBERT 모델과 토크나이저 불러오기
# model_name = "monologg/kobert"
# tokenizer = BertTokenizer.from_pretrained(model_name)
# model = BertModel.from_pretrained(model_name)
#
# # KoBERT를 사용해 문서 임베딩 생성 함수
# def get_bert_embedding(text):
#     tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
#     with torch.no_grad():
#         output = model(**tokens)
#     embedding = output.last_hidden_state[:, 0, :].squeeze().numpy()
#     return embedding
#
# # 유사도 계산 및 저장 함수
# def calculate_and_store_similarity():
#     documents = fetch_html_documents()
#     texts = [preprocess_html(doc['html']) for doc in documents]
#     embeddings = [get_bert_embedding(text) for text in texts]
#
#     # 코사인 유사도 계산
#     similarity_matrix = cosine_similarity(embeddings)
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
#             "similarities": similarities
#         })
#
# # 실행
# calculate_and_store_similarity()


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
        base_id = str(doc['_id'])
        similarities = []

        for jdx, score in enumerate(similarity_matrix[idx]):
            if idx != jdx:
                target_id = str(documents[jdx]['_id'])
                similarities.append({"target_document": target_id, "similarity": float(score)})

        # MongoDB에 저장
        similarity_collection.insert_one({
            "base_document": base_id,
            "similarities": similarities
        })

    return {"message": "Similarity calculations stored successfully."}
