package com.team7.retriever.service;

import com.team7.retriever.dto.ChannelInfoResponse;
import com.team7.retriever.entity.Posts;
import com.team7.retriever.neo4j.service.SavingPromotionService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.HttpStatusCodeException;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;

// Channel Info Module
@Service
@Slf4j
@RequiredArgsConstructor
public class ChannelInfoService {
    private final RestTemplate restTemplate;
    private final ChScrapeService chScrapeService;
    private final PostsService postsService;
    private final SavingPromotionService savingPromotionService;

    // 채널 정보 수집 모듈 호출하는 메서드

    public ChannelInfoResponse getChannelInfo(String inviteToken, String savedPostId) {
        String api = "http://127.0.0.1:5050/telegram/channel/info";
        Map<String, String> requestBody = Map.of("channel_key", inviteToken);
        System.out.println("\t\t\t[ChannelInfoService] inviteToken: " + inviteToken);

        try {
            ResponseEntity<ChannelInfoResponse> response = restTemplate.postForEntity(api, requestBody, ChannelInfoResponse.class);
            System.out.println("\t\t\t[ChannelInfoService] 채널 정보 수집 결과: " + response.getBody());

            ChannelInfoResponse body = response.getBody();
            if (body != null) {
                String title = body.getTitle();
                String status = body.getStatus();
                Long channelId = body.getId();
                System.out.println("\t\t\t[ChannelInfoService] title: " + title);
                System.out.println("\t\t\t[ChannelInfoService] status: " + status);
                System.out.println("\t\t\t[ChannelInfoService] channelId: " + channelId);

                System.out.println("\t\t\t[ChannelInfoService] 채널 검문 결과 (" + title + ") " + status);
                log.info("\t\t\t[ChannelInfoService] 채널 검문 결과 (" + title + ") " + status);

                // 추출된 채널 아이디를 해당 홍보글 데이터에 추가하는 부분
                if (channelId != null && savedPostId != null) {
                    Optional<Posts> optionalPost = postsService.getPostById(savedPostId);
                    if (optionalPost.isPresent()) {
                        Posts post = optionalPost.get();

                        // 기존에 null이면 새로 세팅, 아니면 기존 리스트에 추가
                        List<String> promoChannelIds = post.getPromoChannelId();
                        if (promoChannelIds == null) promoChannelIds = new ArrayList<>();
                        promoChannelIds.add(String.valueOf(channelId));
                        post.setPromoChannelId(promoChannelIds);

                        postsService.addChannelId(post); // 수정된 내용 저장 (채널 아이디 추가하여 저장)
                        System.out.println("\t\t\t[ChannelInfoService] 포스트에 채널 ID 추가 완료 (" + channelId + ")");
                        log.info("\t\t\t[ChannelInfoService] 포스트에 채널 ID 추가 완료 (" + channelId + ")");

                        System.out.println("\t\t\t[ChannelInfoService] Neo4j 작업 시작");
                        savingPromotionService.createPromotionRelation(channelId, savedPostId); // neo4j 작업
                        System.out.println("\t\t\t[ChannelInfoService] Neo4j 작업 완료");
                    } else {
                        System.out.println("\t\t\t[ChannelInfoService] 해당 ID의 포스트를 찾을 수 없습니다: " + savedPostId);
                        log.error("\t\t\t[ChannelInfoService] 해당 ID의 포스트를 찾을 수 없습니다: " + savedPostId);
                    }
                }

                if (status != null && status.equals("active")) {
                    System.out.println("\t\t\t[ChannelInfoService] 채널 스크랩 시작 (" + title + ")");
                    log.info("\t\t\t[ChannelInfoService] 채널 스크랩 시작 (" + title + ")");
                    chScrapeService.channelScrape(inviteToken);
                    System.out.println("\t\t\t[ChannelInfoService] 채널 스크랩 실행 완료 (" + title + ")");
                    log.info("\t\t\t[ChannelInfoService] 채널 스크랩 실행 완료 (" + title + ")");
                }
                return body;
            } else {
                System.out.println("\t\t\t[ChannelInfoService] 응답이 비어있습니다.");
                log.warn("\t\t\t[ChannelInfoService] 응답이 비어있습니다."); // warn? error?
                return null;
            }


        } catch (HttpStatusCodeException e) {
            // 서버(파이썬)에서 4xx, 5xx 에러
            System.out.println("\t\t\t[ChannelInfoService] 서버 오류 발생: " + e.getStatusCode());
            System.out.println("\t\t\t[ChannelInfoService] 오류 응답 내용: " + e.getResponseBodyAsString());
            log.error("\t\t\t[ChannelInfoService] 서버 오류 발생: " + e.getStatusCode());
            log.error("\t\t\t[ChannelInfoService] 오류 응답 내용: " + e.getResponseBodyAsString());
        } catch (Exception e) {
            // 그 외 에러
            System.out.println("\t\t\t[ChannelInfoService] 요청 처리 중 예외 발생: " + e.getMessage());
            log.error("\t\t\t[ChannelInfoService] 요청 처리 중 예외 발생: " + e.getMessage());
        }

        // 에러 나면 null 반환
        return null;
    }
}