package com.team7.retriever.service;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.team7.retriever.entity.PostHtml;
import com.team7.retriever.repository.PostHtmlRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.time.LocalDateTime;
import java.util.Map;
import java.util.Optional;

@Service
@Slf4j
public class HtmlCrawlingService {

    private final RestTemplate restTemplate;
    private final PostHtmlRepository postHtmlRepository;
    private final ObjectMapper objectMapper;

    public HtmlCrawlingService(RestTemplate restTemplate, PostHtmlRepository postHtmlRepository, ObjectMapper objectMapper) {
        this.restTemplate = restTemplate;
        this.postHtmlRepository = postHtmlRepository;
        this.objectMapper = objectMapper;
    }

    public String crawlHtml(String link) {
        String api = "http://127.0.0.1:5050/crawl/html";
        // ResponseEntity<String> response = restTemplate.postForEntity(api, link, String.class);
        Map<String, String> requestBody = Map.of("link", link);
        try {
            ResponseEntity<String> response = restTemplate.postForEntity(api, requestBody, String.class);

            if (response.getStatusCode().is2xxSuccessful() && response.getBody() != null) {
                System.out.println("\t[HtmlCrawlingService] HTML 크롤링 완료");
                log.info("\t[HtmlCrawlingService] HTML 크롤링 완료");
                JsonNode jsonNode = objectMapper.readTree(response.getBody());
                String html = jsonNode.asText();
                // System.out.println("JsonNode TEST");
                // System.out.println(html);
                // System.out.println();
                System.out.println("\t[HtmlCrawlingService] HTML 디코딩 완료");
                log.info("\t[HtmlCrawlingService] HTML 디코딩 완료");
                
                return html; // 크롤링 결과 반환
            } else {
                log.warn("\t[HtmlCrawlingService] HTML is null : " + response.getStatusCode());
                throw new RuntimeException("\t[HtmlCrawlingService] HTML is null : " + response.getStatusCode());
            }
        } catch (Exception e) {
            log.error("\t[HtmlCrawlingService] HTML 크롤링 중 오류 발생: " + e.getMessage(), e);
            throw new RuntimeException("\t[HtmlCrawlingService] HTML 크롤링 중 오류 발생: " + e.getMessage(), e);
        }
    }

    // html 저장 (preprocessService.saveData -> saveHtml)
    public void saveHtml(String postId, String html, String url) {
        LocalDateTime now = LocalDateTime.now();
        PostHtml postHtml = PostHtml.builder()
                .postId(postId)
                .html(html)
                .url(url)
                .createdAt(now)
                .updatedAt(now)
                .build();
        postHtmlRepository.save(postHtml);
        System.out.println("\t[HtmlCrawlingService] " + url + " saved"); // test code
        log.debug("\t[HtmlCrawlingService] " + url + " saved");
    }
}
