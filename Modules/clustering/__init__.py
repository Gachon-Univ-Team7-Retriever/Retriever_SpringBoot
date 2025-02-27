from flask import Blueprint, request, jsonify
from . import post, post_similarity
from .post import dbscan_clustering, collection, db

# Blueprint 설정
cluster_bp = Blueprint('cluster', __name__, url_prefix='/cluster')

# '/post.py' 엔드포인트

@cluster_bp.route('/post', methods=['POST'])
def post_clustering():
    data = request.json
    eps = data.get('eps', 0.4)
    min_samples = data.get('min_samples', 2)

    try:
        result = post.perform_clustering(eps, min_samples)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# '/get_clustered_results' 엔드포인트
@cluster_bp.route('/post_similarity', methods=['POST'])
def post_similarity_calculation():
    try:
        result = post_similarity.calculate_and_store_similarity()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500