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