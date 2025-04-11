package com.team7.retriever.service;


import com.team7.retriever.entity.PostSimilarity;
import com.team7.retriever.repository.PostSimilarityRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@Service
public class PostSimilarityService {

    private final RestTemplate restTemplate;
    private final PostSimilarityRepository postSimilarityRepository;

    public PostSimilarityService(RestTemplate restTemplate, PostSimilarityRepository postSimilarityRepository) {
        this.restTemplate = restTemplate;
        this.postSimilarityRepository = postSimilarityRepository;
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

    public void calculateSimilarity() {
        String api = "http://127.0.0.1:5000/cluster/post_similarity";
        ResponseEntity<Void> response = restTemplate.getForEntity(api, Void.class);
        if (response.getStatusCode().is2xxSuccessful()) {
            System.out.println("[PostSimilarityService] 성공 !");
        } else {
            System.out.println("[PostSimilarityService] 실패");
        }

    }
}