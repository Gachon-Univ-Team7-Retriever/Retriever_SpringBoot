package com.team7.retriever.service;

// import com.team7.retriever.dto.CrawlGoogleResponse;
import com.team7.retriever.dto.WebCrawlingRequest;
import com.team7.retriever.dto.WebCrawlingResponse;
import com.team7.retriever.entity.PostHtml;
import com.team7.retriever.repository.PostHtmlRepository;
import org.springframework.http.HttpEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Map;
import java.util.Optional;

@Service
public class WebCrawlingService {
    private final RestTemplate restTemplate;
    private final PostHtmlRepository htmlRepository;

    public WebCrawlingService(RestTemplate restTemplate, PostHtmlRepository htmlRepository) {
        this.restTemplate = restTemplate;
        this.htmlRepository = htmlRepository;
    }

    public WebCrawlingResponse webCrawling(WebCrawlingRequest webCrawlingRequest) {
        String api = "http://127.0.0.1:5000/crawl/links";

        HttpEntity<WebCrawlingRequest> request = new HttpEntity<>(webCrawlingRequest);
        ResponseEntity<WebCrawlingResponse> response = restTemplate.postForEntity(api, request, WebCrawlingResponse.class);

        WebCrawlingResponse results = response.getBody();
        if (results != null) {
            List<String> google = results.getGoogle();
            List<String> telegram = results.getTelegram();

            PostHtml postHtml;
            LocalDateTime now = LocalDateTime.now();
            int inserted = 0;
            int updated = 0;

            /*
            // google
            System.out.println("Google --------------");
            for (CrawlGoogleResponse googleResponse : google) {
                // System.out.println("\t- " + googleResponse.getHtml());
                System.out.println("\t- html OK");
                System.out.println("\t  " + googleResponse.getUrl());

                String html = googleResponse.getHtml();
                String url = googleResponse.getUrl();
                String id = "html_" + url;

                Optional<PostHtml> existingEntry = htmlRepository.findById(id);
                if (!existingEntry.isPresent()) {
                    postHtml = new PostHtml();
                    postHtml.setId(id);
                    postHtml.setPostId("post_" + url);
                    postHtml.setCreatedAt(now);
                    postHtml.setUrl(url);
                    inserted += 1;
                } else  { // DB에 이미 존재하는 경우 (update)
                    System.out.println(id + " is already exist"); // test code
                    postHtml = existingEntry.get();
                    updated += 1;
                }
                postHtml.setHtml(html);
                postHtml.setUpdatedAt(now);
                htmlRepository.save(postHtml);
                System.out.println(id + " saved"); // test code
            }

             */

            // test code
            /*
            System.out.println("Successfully saved !");
            System.out.println("Total :");
            System.out.println(inserted + " inserted");
            System.out.println(updated + " updated");
            System.out.println();

             */

            // google
            System.out.println("Google --------------");
            if (google != null) {
                for (String googleResponse : google) {
                    System.out.println("\t- " + googleResponse);
                }
            } else {
                System.out.println("No google found");
            }

            // telegram
            System.out.println("Telegram --------------");
            if (telegram != null) {
                for (String telegramResponse : telegram) {
                    System.out.println("\t- " + telegramResponse);
                    // channel scrape service call
                }
            } else {
                System.out.println("No telegram found");
            }
        }


        return response.getBody();
    }

    /*
    public List<Map<String, Object>> webCrawling(String keyword) {
        // Flask API URL
        String api = "http://127.0.0.1:5000/crawl/google?query=t.me " + keyword;

        // Flask API 호출
        ResponseEntity<List> response = restTemplate.getForEntity(api, List.class);

        // 데이터 처리 및 출력
        List<Map<String, Object>> results = response.getBody();
        if (results != null) {
            int updated = 0; // test code
            int inserted = 0; // test code
            for (Map<String, Object> result : results) {
                String url = (String) result.get("url");

                String id = "html_" + url;
                LocalDateTime now = LocalDateTime.now();

                PostHtml postHtml;
                Optional<PostHtml> existingEntry = htmlRepository.findById(id);
                if (!existingEntry.isPresent()) { // DB에 존재하지 않는 경우 (insert)
                    System.out.println(id + " not found"); // test code
                    postHtml = new PostHtml();
                    postHtml.setId(id);
                    postHtml.setPostId("post_" + url);
                    postHtml.setCreatedAt(now);
                    postHtml.setUrl(url);
                    inserted += 1;
                } else  { // DB에 이미 존재하는 경우 (update)
                    System.out.println(id + " is already exist"); // test code
                    postHtml = existingEntry.get();
                    updated += 1;
                }
                postHtml.setHtml((String) result.get("html"));
                postHtml.setUpdatedAt(now);
                htmlRepository.save(postHtml);
                System.out.println(id + " saved"); // test code
            }
            // test code
            System.out.println("Successfully saved !");
            System.out.println("Total :");
            System.out.println(inserted + " inserted");
            System.out.println(updated + " updated");
        }

        // 결과 반환
        return response.getBody();
    }
    */
}
