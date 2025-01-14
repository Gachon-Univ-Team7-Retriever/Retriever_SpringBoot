package com.team7.retriever.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import com.team7.retriever.entity.Posts;
import com.team7.retriever.repository.PostsRepository;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.time.LocalDateTime;
import java.util.Optional;

@Service
public class PreprocessService {
    private final RestTemplate restTemplate;
    private final PostsRepository postsRepository;
    private final ObjectMapper objectMapper;

    public PreprocessService(RestTemplate restTemplate, PostsRepository postsRepository, ObjectMapper objectMapper) {
        this.restTemplate = restTemplate;
        this.postsRepository = postsRepository;
        this.objectMapper = objectMapper;
    }

    public String postPreprocess(String url, String requestData) {
        System.out.println(requestData);

        String api = "http://127.0.0.1:5000/preprocess/extract/web_promotion";

        ObjectMapper objectMapper = new ObjectMapper();
        ObjectNode jsonNode = objectMapper.createObjectNode();
        jsonNode.put("html", requestData);

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> requestEntity = new HttpEntity<>(jsonNode.toString(), headers);

        ResponseEntity<String> response = restTemplate.postForEntity(api, requestEntity, String.class);

        // return response.getBody(); // 기본 반환 코드 (인코딩 문제 발생)

        LocalDateTime now = LocalDateTime.now();

        String id = "post_" + url;
        Posts posts;
        Optional<Posts> existingEntry = postsRepository.findById(response.getBody());

        if (!existingEntry.isPresent()) {
            System.out.println(id + "\tPost not found");
            posts = new Posts();
            posts.setId(id);
            posts.setLink(url);
            posts.setTag("tag");
            posts.setSiteName("site name");
            posts.setTitle("title");
            posts.setPromoSiteLink("promotion site link");
            posts.setPromoSiteName("promo site name");
            posts.setAuthor("author");
            posts.setTimestamp(null);
            posts.setCreatedAt(now);
        } else {
            System.out.println(id + "\tPost found");
            posts = existingEntry.get();
        }
        // posts.setContent(response.getBody());
        posts.setUpdatedAt(now);
        // postsRepository.save(posts);

        String content;
        try {
            JsonNode jsonNode2 = objectMapper.readTree(response.getBody()); // 파싱
            // 필드 추출
            content = jsonNode2.get("promotion_content").asText();
            posts.setContent(content);
            postsRepository.save(posts);
            System.out.println("Successfully saved !");
            return content;
        } catch (Exception e) {
            posts.setContent(response.getBody());
            postsRepository.save(posts);
            System.out.println("Decoding failed, saved as it.");
            throw new RuntimeException("Failed to parse response", e);
        }


    }
}
