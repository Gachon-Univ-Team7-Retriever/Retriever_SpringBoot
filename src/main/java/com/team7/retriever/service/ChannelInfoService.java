package com.team7.retriever.service;

import com.team7.retriever.dto.ChannelInfoResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.HttpStatusCodeException;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

// Channel Info Module
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

        try {
            ResponseEntity<ChannelInfoResponse> response = restTemplate.postForEntity(api, requestBody, ChannelInfoResponse.class);
            /*
            ResponseEntity<Map> response = restTemplate.postForEntity(api, requestBody, Map.class);
            Map body = response.getBody();
            System.out.println(body);

             */

            ChannelInfoResponse body = response.getBody();
            if (body != null) {
                String title = body.getTitle();
                String status = body.getStatus();
                System.out.println("\t\t\t[ChannelInfoService] 채널 검문 결과 (" + title + ") " + status);

                if (status != null && status.equals("active")) {
                    System.out.println("\t\t\t[ChannelInfoService] 채널 스크랩 시작 (" + title + ")");
                    chScrapeService.channelScrape(inviteToken);
                    System.out.println("\t\t\t[ChannelInfoService] 채널 스크랩 실행 완료 (" + title + ")");
                }
                return body;
            } else {
                System.out.println("\t\t\t[ChannelInfoService] 응답이 비어있습니다.");
                return null;
            }


        } catch (HttpStatusCodeException e) {
            // 서버(파이썬)에서 4xx, 5xx 에러
            System.out.println("\t\t\t[ChannelInfoService] 서버 오류 발생: " + e.getStatusCode());
            System.out.println("\t\t\t[ChannelInfoService] 오류 응답 내용: " + e.getResponseBodyAsString());
        } catch (Exception e) {
            // 그 외 에러
            System.out.println("\t\t\t[ChannelInfoService] 요청 처리 중 예외 발생: " + e.getMessage());
        }

        // 에러 나면 null 반환
        return null;
    }
}