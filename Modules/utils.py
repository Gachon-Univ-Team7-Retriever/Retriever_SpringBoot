from flask import jsonify

from itertools import zip_longest

def merge_lists_remove_duplicates(lists):
    seen = set()  # 중복 체크용
    result = []

    # zip_longest를 사용하여 여러 리스트를 병렬로 순회
    for items in zip_longest(*lists, fillvalue=None):
        for item in items:
            if item is not None and item not in seen:  # 중복 제거
                seen.add(item)
                result.append(item)

    return result


def confirm_request(data, required: list):
    if not data:
        return jsonify({"error": "Please provide JSON request body."}), 400
    for key in required:
        if key not in data:
            return jsonify({"error": f"Please provide '{key}' in the JSON request body."}), 400

import uuid
import typing
def generate_integer_id64(existing_ids:typing.Iterable[int]=None):
    """64비트 무작위 정수 ID를 생성해서 반환하는 함수."""
    # uuid4()를 사용하여 무작위 UUID 생성 후, 정수형으로 변환
    if not existing_ids:
        return uuid.uuid4().int % (1 << 63)
    while (new_id:=uuid.uuid4().int % (1 << 63)) in existing_ids:
        pass
    return new_id


def compare_dicts_sorted(
        dict1: dict[str, list[int]],
        dict2: dict[str, list[int]]
) -> bool:
    """두 개의 딕셔너리를 비교해서 원소가 완벽히 동일하면 참을, 그렇지 않으면 거짓을 반환하는 함수."""
    # 두 딕셔너리의 키 집합이 동일한지 확인
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # 각 키별로 정렬된 리스트를 비교 (중복을 고려)
    for key in dict1:
        if sorted(dict1[key]) != sorted(dict2[key]):
            return False

    return True