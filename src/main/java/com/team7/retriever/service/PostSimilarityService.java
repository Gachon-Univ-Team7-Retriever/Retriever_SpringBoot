package com.team7.retriever.service;


import com.team7.retriever.entity.PostSimilarity;
import com.team7.retriever.repository.PostSimilarityRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PostSimilarityService {

    @Autowired
    private PostSimilarityRepository postSimilarityRepository;

    public PostSimilarityService(PostSimilarityRepository repository) {
        this.postSimilarityRepository = repository;
    }

    // 전체 조회
    public List<PostSimilarity> getAllPostSimilarities() {
        List<PostSimilarity> allPosts = postSimilarityRepository.findAll();
        allPosts.forEach(this::sortSimilarPostsBySimilarity);
        return allPosts;
    }

    // 아이디로 조회
    public PostSimilarity getPostSimilarityById(String id) {
        PostSimilarity postSimilarity = postSimilarityRepository.findById(id).orElse(null);
        if (postSimilarity != null) {
            sortSimilarPostsBySimilarity(postSimilarity);
        }
        return postSimilarity;
    }

    // 포스트 아이디로 조회
    public PostSimilarity getPostSimilarityByPostId(String postId) {
        PostSimilarity postSimilarity = postSimilarityRepository.findByPostId(postId);
        if (postSimilarity != null) {
            sortSimilarPostsBySimilarity(postSimilarity);
        }
        return postSimilarity;
    }

    // 유사도 높은 순서로 정렬
    private void sortSimilarPostsBySimilarity(PostSimilarity postSimilarity) {
        postSimilarity.getSimilarPosts().sort((a, b) -> Double.compare(b.getSimilarity(), a.getSimilarity()));
    }
}