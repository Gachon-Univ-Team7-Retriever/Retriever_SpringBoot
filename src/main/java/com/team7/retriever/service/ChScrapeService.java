package com.team7.retriever.service;

import com.team7.retriever.dto.ChDataResponse;
import com.team7.retriever.repository.ChDataRepository;
import com.team7.retriever.repository.ChInfoRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Map;
import java.util.Objects;

@Service
@Slf4j
public class ChScrapeService {
    private final RestTemplate restTemplate;

    public ChScrapeService(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    // 스케줄 1 에서 실행되는 메서드 (channelInfo -> channelScrape)
    public void channelScrape(String channelKey) {
        // String infoAPI = "http://127.0.0.1:5000/telegram/channel/info";
        String api = "http://127.0.0.1:5000/telegram/channel/scrape";

        Map<String, String> requestBody = Map.of("channel_key", channelKey);
        log.debug("\t\t\t\t[ChScrapeService] channel_key: " + channelKey);
        // ResponseEntity<String> infoResponse = restTemplate.postForEntity(infoAPI, requestBody, String.class); // 사용X
        ChDataResponse response = restTemplate.postForObject(api, requestBody, ChDataResponse.class);
        String message = Objects.requireNonNull(response).getMessage(); // 응답이 비어있을 수 있음
        String status = response.getStatus();
        System.out.println("\t\t\t\t[ChScrapeService] " + message);
        System.out.println("\t\t\t\t[ChScrapeService] 채널 " + channelKey + " 스크랩 상태: " +  status);

        log.info("\t\t\t\t[ChScrapeService] " + message);
        log.info("\t\t\t\t[ChScrapeService] 채널 " + channelKey + " 스크랩 상태: " +  status);
    }
}
