package com.team7.retriever.service;

import com.team7.retriever.dto.ChannelCheckResponse;
import com.team7.retriever.dto.ChannelInfoResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@Service
public class ChannelInfoService {
    private final RestTemplate restTemplate;
    private final ChScrapeService chScrapeService;

    public ChannelInfoService(RestTemplate restTemplate, ChScrapeService chScrapeService) {
        this.restTemplate = restTemplate;
        this.chScrapeService = chScrapeService;
    }

    public ChannelInfoResponse getChannelInfo(String inviteToken) {
        String api = "http://127.0.0.1:5000/telegram/channel/info";
        Map<String, String> requestBody = Map.of("channel_key", inviteToken);
        ResponseEntity<ChannelInfoResponse> response = restTemplate.postForEntity(api, requestBody, ChannelInfoResponse.class);

        String title = response.getBody().getTitle();
        String status = response.getBody().getStatus();
        System.out.println("\t\t\t[ChannelInfoService] 채널 검문 결과 (" + title + ") " + status);

        if (status != null) {
            if (status.equals("active")) {
                System.out.println("\t\t\t[ChannelInfoService] 채널 스크랩 시작 (" + title + ")");
                // chScrapeService.channelScrape(channel); // 채널 스크랩 모듈 실행 // 소요 시간 때문에 주석 처리, 풀어줘야 함 !
                System.out.println("\t\t\t[ChannelInfoService] 채널 스크랩 실행 완료 (" + title + ")"); // 처리 상태 X / 실행 완료 확인용
            }
        }
        return response.getBody();
    }
}
