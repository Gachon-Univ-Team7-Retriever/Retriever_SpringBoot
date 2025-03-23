# from pymongo import MongoClient
# from transformers import BertTokenizer, BertModel
# from bs4 import BeautifulSoup
# from sklearn.metrics.pairwise import cosine_similarity
# import torch
# import numpy as np
# import networkx as nx
# from community import community_louvain
#
# # MongoDB 연결
# client = MongoClient("mongodb://localhost:27017/")
# db = client['local']
# collection = db['channels']
# similarity_collection = db['channel_similarity']
#
# # KoBERT 모델 및 토크나이저 로드
# model_name = "monologg/kobert"
# tokenizer = BertTokenizer.from_pretrained(model_name)
# model = BertModel.from_pretrained(model_name)
#
# # 마약 키워드 가중치 설정
# drug_keywords = {
#     '코카인': 2.0,
#     '메스암페타민': 2.0,
#     '펜타닐': 2.5,
#     'LSD': 1.8,
#     '엑스터시': 2.0
# }
#
# # HTML 전처리 및 클린 텍스트 생성
# def preprocess_html(html_content):
#     soup = BeautifulSoup(html_content, 'html.parser')
#     text = soup.get_text(separator=' ').strip()
#     text = ' '.join(text.split())  # 중복 공백 제거
#     return text
#
# # 가중치 적용 텍스트 전처리 (단어 가중치 적용)
# def apply_keyword_weight(text):
#     words = text.split()
#     weighted_words = []
#     for word in words:
#         weight = drug_keywords.get(word, 1.0)
#         weighted_words.append((word + ' ') * int(weight))
#     return ' '.join(weighted_words)
#
# # KoBERT 임베딩 생성 (평균 풀링 적용)
# def get_bert_embedding(text):
#     tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding="max_length")
#     with torch.no_grad():
#         output = model(**tokens)
#     embeddings = output.last_hidden_state.squeeze(0)
#     return embeddings.mean(dim=0).numpy()  # 평균 풀링 적용
#
# # 채널 유사도 분석 및 저장 (MongoDB 성능 최적화)
# def calculate_and_store_similarity():
#     documents = list(collection.find({}, {"_id": 1, "html": 1}))
#     texts = [apply_keyword_weight(preprocess_html(doc['html'])) for doc in documents]
#     embeddings = [get_bert_embedding(text) for text in texts]
#
#     # 코사인 유사도 계산
#     similarity_matrix = cosine_similarity(embeddings)
#
#     # 그래프 생성 및 Louvain 커뮤니티 탐지
#     G = nx.Graph()
#     for idx, doc in enumerate(documents):
#         G.add_node(doc['_id'], label=f"Channel_{idx+1}")
#         for jdx, score in enumerate(similarity_matrix[idx]):
#             if idx != jdx and score > 0.75:
#                 G.add_edge(doc['_id'], documents[jdx]['_id'], weight=score)
#
#     # Louvain 알고리즘 적용 (resolution 파라미터 조정 가능)
#     partition = community_louvain.best_partition(G, resolution=1.0)
#
#     # 결과 저장 (insert_many로 성능 향상)
#     similarity_data = [{"channel_id": node, "community": community} for node, community in partition.items()]
#     if similarity_data:
#         similarity_collection.insert_many(similarity_data)
#
#     return {"message": "Channel similarity and communities stored successfully."}
#
# # 실행
# if __name__ == "__main__":
#     try:
#         result = calculate_and_store_similarity()
#         print(result)
#     except Exception as e:
#         print(f"Error: {e}")
# ------------------------------------------------------------------------------------------




from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
import torch
import numpy as np
import networkx as nx
from community import community_louvain
from bs4 import BeautifulSoup

# KoBERT 모델 및 토크나이저 로드
model_name = "monologg/kobert"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# 마약 키워드 가중치 설정
drug_keywords = {
    '코카인': 3.0,
    '메스암페타민': 3.0,
    '펜타닐': 3.0,
    'LSD': 3.0,
    '엑스터시': 3.0,
    '순도': 2.0
}

# 예시 채널 데이터 (HTML 형식)
channels = [
    {
        "_id": "channel_1",
        "html": "<html><body>"
                "<p>A: 요즘 코카인 가격 많이 올랐다며?</p>"
                "<p>B: 맞아, 공급이 줄어서 그런가 봐.</p>"
                "<p>A: 근데 진짜 위험한 거 알지? 요즘 단속도 심하대.</p>"
                "</body></html>"
    },
    {
        "_id": "channel_2",
        "html": "<html><body>"
                "<p>C: 메스암페타민 구하는 곳 아는 사람?</p>"
                "<p>D: 그거 조심해야 돼. 걸리면 큰일 난다.</p>"
                "<p>C: 알지. 근데 요즘 순도 높은 거 찾기가 힘들어서.</p>"
                "</body></html>"
    },
    {
        "_id": "channel_3",
        "html": "<html><body>"
                "<p>E: LSD 처음 해보는데 이거 환각 진짜 장난 아니다.</p>"
                "<p>F: 그러게, 조심해. 잘못하면 며칠 가는 경우도 있대.</p>"
                "<p>E: 그래도 느낌 쩐다. 다른 사람들도 많이 해?</p>"
                "</body></html>"
    },
    {
        "_id": "channel_4",
        "html": "<html><body>"
                "<p>G: 엑스터시 클럽에서 해본 사람 있어?</p>"
                "<p>H: 예전에 몇 번 해봤는데, 조심해야해.</p>"
                "<p>G: 진짜? 근데 요즘 순도가 떨어졌다는 얘기 많던데.</p>"
                "</body></html>"
    },
    {
        "_id": "channel_5",
        "html": "<html><body>"
                "<p>I: 오늘 영화 뭐 볼까?</p>"
                "<p>J: 코미디 한 편 어때? 요즘 스트레스 너무 받았어.</p>"
                "<p>I: 좋아. 넷플릭스에 괜찮은 거 있나 보자.</p>"
                "</body></html>"
    }
]


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
    tokens = tokenizer(text, return_tensors="pt", truncation=True, max_length=256, padding="max_length")
    with torch.no_grad():
        output = model(**tokens)
    embeddings = output.last_hidden_state[:, 0, :]
    return embeddings.squeeze(0).numpy()


# 채널 유사도 분석 및 커뮤니티 탐지
def calculate_and_store_similarity():
    texts = [apply_keyword_weight(preprocess_html(doc['html'])) for doc in channels]
    embeddings = [get_bert_embedding(text) for text in texts]

    # 코사인 유사도 계산
    similarity_matrix = cosine_similarity(embeddings)

    # 그래프 생성 및 Louvain 커뮤니티 탐지
    G = nx.Graph()
    for idx, doc in enumerate(channels):
        G.add_node(doc['_id'], label=f"Channel_{idx+1}")
        for jdx, score in enumerate(similarity_matrix[idx]):
            if idx != jdx and score > 0.93:  # 유사도 threshold를 0.75로 설정
                G.add_edge(doc['_id'], channels[jdx]['_id'], weight=score)

    # Louvain 알고리즘 적용 (resolution 파라미터 조정 가능)
    partition = community_louvain.best_partition(G, resolution=1.1)

    print("Similarity Matrix:\n", similarity_matrix)

    # 결과 출력 (예시 데이터에 대한 커뮤니티 정보)
    similarity_data = [{"channel_id": node, "community": community} for node, community in partition.items()]
    return similarity_data

# 실행
if __name__ == "__main__":
    try:
        result = calculate_and_store_similarity()
        print("Channel Similarity and Communities:")
        for res in result:
            print(res)
    except Exception as e:
        print(f"Error: {e}")
