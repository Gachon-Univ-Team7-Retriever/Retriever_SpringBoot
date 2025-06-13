package com.team7.retriever.service;


import com.team7.retriever.entity.PostSimilarity;
import com.team7.retriever.repository.PostSimilarityRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Map;

@Service
@Slf4j
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
        System.out.println("[PostSimilarityService] API 호출");
        log.info("[PostSimilarityService] API 호출");
        String api1 = "http://127.0.0.1:5000/cluster/post_update";
        String api2 = "http://127.0.0.1:5000/cluster/post_cluster";

        ResponseEntity<Map> response = restTemplate.postForEntity(api1, null, Map.class);

        if (response.getStatusCode().is2xxSuccessful() && response.getBody() != null) {
            String message = response.getBody().get("message").toString();
            System.out.println("[PostSimilarityService] message: " + message);
            System.out.println("[PostSimilarityService] 성공 !");
        } else {
            System.out.println("[PostSimilarityService] 실패");
        }
        System.out.println("[PostSimilarityService] 실행 완료");

        ResponseEntity<Map> response2 = restTemplate.postForEntity(api1, null, Map.class);

        if (response2.getStatusCode().is2xxSuccessful() && response2.getBody() != null) {
            String message = response2.getBody().get("message").toString();
            int totla_document = Integer.parseInt(response2.getBody().get("total_documents").toString());
            int noise_document = Integer.parseInt(response2.getBody().get("noise_documents").toString());
            float silhouette_score = Float.parseFloat(response2.getBody().get("silhouette_score").toString());

            System.out.println("[PostSimilarityService] message: " + message);
            System.out.println("[PostSimilarityService] totla_document: " + totla_document);
            System.out.println("[PostSimilarityService] noise_document: " + noise_document);
            System.out.println("[PostSimilarityService] silhouette_score: " + silhouette_score);

            System.out.println("[PostSimilarityService] 성공 !");
        } else {
            System.out.println("[PostSimilarityService] 실패");
        }


        System.out.println("[PostSimilarityService] 실행 완료");

    }
}