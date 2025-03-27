package com.team7.retriever.repository;

import com.team7.retriever.entity.PostSimilarity;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PostSimilarityRepository extends MongoRepository<PostSimilarity, String> {

    // 포스트 아이디로 조회
    PostSimilarity findByPostId(String postId);
}