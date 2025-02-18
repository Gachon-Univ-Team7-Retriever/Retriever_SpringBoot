import re
from fastapi import FastAPI, Form
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
from typing import List

# FastAPI 애플리케이션 생성
app = FastAPI()

# BERT 모델과 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# 텍스트 전처리 함수
def preprocess_text(text):
    """
    입력 텍스트를 전처리
    - 특수문자 제거, 소문자 변환, 공백 정리
    """
    text = re.sub(r'[^\w\s]', '', text)  # 특수문자 제거
    text = re.sub(r'\s+', ' ', text)  # 여러 공백을 하나로 축소
    return text.lower().strip()

# BERT 임베딩 생성 함수
def get_bert_embedding(text, model, tokenizer):
    """
    입력 텍스트를 BERT 임베딩으로 변환
    """
    text = preprocess_text(text)
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].numpy()  # CLS 토큰 벡터 반환

# 코사인 유사도 계산 함수
def calculate_similarity(text1, text2):
    """
    두 텍스트 간의 코사인 유사도 계산
    """
    embedding1 = get_bert_embedding(text1, model, tokenizer)
    embedding2 = get_bert_embedding(text2, model, tokenizer)
    similarity = cosine_similarity(embedding1, embedding2)
    return float(similarity[0][0])

# 채팅방 비교 함수
def compare_chat_rooms(chat_room_a: List[str], chat_room_b: List[str]):
    """
    두 채팅방 간의 유사도를 계산
    """
    total_similarity = 0
    pairwise_comparisons = []
    count = 0

    for message_a in chat_room_a:
        for message_b in chat_room_b:
            similarity = calculate_similarity(message_a, message_b)
            pairwise_comparisons.append({
                "message_a": message_a,
                "message_b": message_b,
                "similarity": similarity
            })
            total_similarity += similarity
            count += 1

    # 평균 유사도 계산
    average_similarity = total_similarity / count if count > 0 else 0
    return {
        #"pairwise_comparisons": pairwise_comparisons,
        "average_similarity": average_similarity
    }

# FastAPI 엔드포인트 정의
@app.post("/compare_chat_rooms/")
async def compare_chat_rooms_endpoint(
        chat_room_a: List[str] = Form(...),
        chat_room_b: List[str] = Form(...),
):
    """
    두 채팅방 메시지 리스트를 비교하여 유사도 분석
    """
    result = compare_chat_rooms(chat_room_a, chat_room_b)
    return result
