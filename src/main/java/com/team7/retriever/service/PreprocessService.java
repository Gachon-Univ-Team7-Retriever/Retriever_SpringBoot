package com.team7.retriever.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.team7.retriever.dto.PreprocessResponse;
import com.team7.retriever.entity.Posts;
import com.team7.retriever.repository.PostsRepository;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.net.URL;
import java.time.LocalDateTime;
import java.util.*;

@Service
@AllArgsConstructor
public class PreprocessService {
    private final RestTemplate restTemplate;
    private final PostsRepository postsRepository;
    private final PostsService postsService;
    private final ObjectMapper objectMapper;
    private final HtmlCrawlingService htmlCrawlingService;
    private final ChInfoService chInfoService;
    private final ChannelInfoService channelInfoService;

    // 스케줄 2 - 데이터 업데이트
    public String updatePreprocess(String html, String link, String title, String source) {
        String api = "http://127.0.0.1:5050/preprocess/extract/web-promotion";

        Map<String, String> requestBody = Map.of("html", html);
        ResponseEntity<String> response = restTemplate.postForEntity(api, requestBody, String.class);
        try {

            if (!response.getStatusCode().is2xxSuccessful() || response.getBody() == null) { // 다시 확인 필요
                throw new RuntimeException("\t\t[PreprocessService] HTML 전처리 실패: \" + response.getStatusCode()");
            }
            JsonNode jsonNode = objectMapper.readTree(response.getBody());
            String content = jsonNode.get("promotion_content").asText(null); // null 기본값 사용 (promotion_content가 없거나 null인 경우)
            List<String> telegrams = objectMapper.convertValue(
                    jsonNode.get("telegrams"),
                    objectMapper.getTypeFactory().constructCollectionType(List.class, String.class)
            );

            System.out.println("\t\t[PreprocessService] 전처리 결과: " + content);
            if (Objects.equals(content, "null") || content == null) {
                System.out.println("\t\t[PreprocessService] 마약 관련 홍보글이 아닙니다!");
                // 해당 링크 모든 데이터 삭제됨 상태로 설정
                setDeleted(link);
                System.out.println("\t\t[PreprocessService] 홍보글 삭제 처리 완료");
            } else { // 마약 관련 홍보글인 경우
                System.out.println("\t\t[PreprocessService] 마약 관련 홍보글입니다!");
                // 해당 링크 모든 데이터 updatedAt 업데이트
                // 해당 링크로 새로운 데이터 DB에 저장
                updateData(html, link, title, source, content, telegrams);
                System.out.println("\t\t[PreprocessService] 데이터 업데이트 완료");
            }
            return content;
        } catch (JsonProcessingException e) {
            throw new RuntimeException("\t\t[PreprocessService] JSON 파싱 중 오류 발생: " + e.getMessage(), e);
        } catch (Exception e) {
            throw new RuntimeException("\t\t[PreprocessService] HTML 전처리 중 오류 발생: " + e.getMessage(), e);
        }
    }

    // 데이터 삭제됨 상태로 변경
    private void setDeleted(String link) {
        List<Posts> posts = postsService.getPostsByLink(link);
        LocalDateTime now = LocalDateTime.now();
        for (Posts post : posts) {
            post.markAsDeleted(now);
            postsRepository.save(post);
        }
        System.out.println("\t\t[PreprocessService] " + posts.size() + "개의 데이터를 업데이트, 삭제 상태로 변경 완료");
    }

    /*
     게시물이 비어있으면 false 반환
     content가 변경되었으면 true, 아니면 false 리턴
     */
    private boolean isContentUpdated(List<Posts> posts, String newContent) {
        if (posts.isEmpty()) return false;
        Posts latestPost = posts.get(posts.size() - 1);
        return !latestPost.getContent().equals(newContent);
    }

    // 데이터 업데이트
    // 1. 업데이트 시각 변경
    // 2. 업데이트 사항 있으면 새 데이터 저장 (데이터 저장 메서드 호출)
    private void updateData(String html, String link, String title, String source, String content, List<String> telegrams) {
        List<Posts> posts = postsService.getPostsByLink(link);
        for (Posts post : posts) {
            post.updateTimestampToNow(); // 테스트 필요
        }
        System.out.println("\t\t[PreprocessService] " + posts.size() + "개의 데이터 업데이트 시각 변경 완료");

        if (isContentUpdated(posts, content)) { // 본문 내용이 동일하지 않으면
            System.out.println("\t\t[PreprocessService] 홍보글에 업데이트 사항이 있습니다");
            String savedId = saveData(html, link, title, source, content, telegrams);
            System.out.println("\t\t[PreprocessService] 최신 데이터 저장 완료");
            getChannelInfo(telegrams, savedId);
        }
    }

    // 링크에서 도메인 추출
    public String extractDomain(String link) {
        try {
            URL url = new URL(link);
            String domain = url.getHost();

            // domain = domain.replace("www.", "");

            System.out.println("\t\t[PreprocessService] 도메인 추출 완료 : " + domain);
            return domain;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    // 데이터 새로 저장
    private String saveData(String html, String link, String title, String source, String content, List<String> telegrams) {
        Posts post = Posts.builder()
                .link(link)
                .tag(null) // X
                .source(source)
                .siteName(extractDomain(link))
                .title(title)
                .content(content)
                .promoSiteLink(List.copyOf(telegrams))
                .promoChannelId(null) // 채널 정보 수집 후에 저장됨
                .author(null) // X
                .timestamp(null) // X
                .createdAt(LocalDateTime.now())
                .updatedAt(LocalDateTime.now())
                .deletedAt(null)
                .deleted(false)
                .build();

        Posts saved = postsRepository.save(post);
        String savedId = saved.getId();
        System.out.println("\t\t[PreprocessService] 저장된 게시글 ID: " + savedId);

        htmlCrawlingService.saveHtml(savedId, html, link);

        return savedId;
    }

    public void getChannelInfo(List<String> telegrams, String savedId) {
        System.out.println("\t\t[PreprocessService] 추출된 채널: " + telegrams);
        if (!telegrams.isEmpty()) {
            for (String telegram : telegrams) {
                if (chInfoService.isChannelExists(telegram)) { // DB에 이미 정보가 존재하면 스킵
                    System.out.println("\t\t[PreprocessService] DB에 해당 채널이 이미 존재합니다 !");
                    // ChInfo chInfo = chInfoRepository.findById(telegram).get();
                    // chInfo.setPromoCount(chInfo.getPromoCount() + 1);
                } else { // DB에 해당 채널 아이디가 존재하지 않으면 채널 정보 수집 모듈 실행
                    // channelCheckService.checkChannel(telegram);
                    System.out.println("\t\t[PreprocessService] channelInfo 실행");
                    channelInfoService.getChannelInfo(telegram, savedId);
                    System.out.println("\t\t[PreprocessService] channelInfo 실행 완료");
                }
            }
        }
    }

    // 스케줄 1
    // 1. html 전처리
    // 2. 본문에서 텔레그램 채널 추출 시
    //  2.1. 해당 채널이 DB에 있으면 홍보글 개수 업데이트
    //  2.2. 없으면 검문 서비스 호출
    public void htmlPreprocess(String url, String title, String source, String html) {
        String api = "http://127.0.0.1:5050/preprocess/extract/web-promotion";

        Map<String, String> requestBody = Map.of("html", html);
        // System.out.println("[DEBUG] HTML Preprocess RequestBody");
        // System.out.println(requestBody);

        try {
            ResponseEntity<String> response = restTemplate.postForEntity(api, requestBody, String.class);
            if (!response.getStatusCode().is2xxSuccessful() || response.getBody() == null) { // 다시 확인 필요
                throw new RuntimeException("\t\t[PreprocessService] HTML 전처리 실패: \" + response.getStatusCode()");
            }
            JsonNode jsonNode = objectMapper.readTree(response.getBody());
            String content = jsonNode.get("promotion_content").asText(null); // null 기본값 사용 (promotion_content가 없거나 null인 경우)
            List<String> telegrams = objectMapper.convertValue(
                    jsonNode.get("telegrams"),
                    objectMapper.getTypeFactory().constructCollectionType(List.class, String.class)
            );

            // 기존 post 아이디 설정하고, 아이디로 데이터 조회하는 부분
            // String id = "post_" + url; // 아이디는 자동 생성 -> 아이디 생성 부분 삭제
            // Optional<Posts> existingEntry = postsRepository.findById(id); // 존재하지 않아야 실행되도록 구현됨 -> 삭제

            System.out.println("\t\t[PreprocessService] 전처리 결과: " + content);
            if (Objects.equals(content, "null") || content == null) {
                System.out.println("\t\t[PreprocessService] 마약 관련 홍보글이 아닙니다!");
            } else { // 마약 관련 홍보글인 경우
                System.out.println("\t\t[PreprocessService] 마약 관련 홍보글입니다!");
                String savedId = saveData(html, url, title, source, content, telegrams); // 저장

                System.out.println("\t\t[PreprocessService] " + url + " saved");

                getChannelInfo(telegrams, savedId);
            }
        } catch (JsonProcessingException e) {
            throw new RuntimeException("\t\t[PreprocessService] JSON 파싱 중 오류 발생: " + e.getMessage(), e);
        } catch (Exception e) {
            throw new RuntimeException("\t\t[PreprocessService] HTML 전처리 중 오류 발생: " + e.getMessage(), e);
        }
    }

    public void htmlPreprocessAi(String url, String title, String source, String html) {
        String api = "http://127.0.0.1:5050//preprocess/extract/web-promotion/openai";

        Map<String, String> requestBody = Map.of("html", html);

        try {
            ResponseEntity<PreprocessResponse> response = restTemplate.postForEntity(
                    api,
                    requestBody,
                    PreprocessResponse.class
            );

            if (!response.getStatusCode().is2xxSuccessful() || response.getBody() == null) {
                System.out.println("\t\t[PreprocessService] HTML 전처리(AI) 실패: " + response.getStatusCode());
            } else {
                PreprocessResponse responseDto = response.getBody();

                Boolean classificationResult = responseDto.getClassificationResult();
                String content = responseDto.getPromotionContent();
                List<String> telegrams = responseDto.getTelegrams();

                System.out.println("\t\t[PreprocessService] (AI) 전처리 결과: " + content);

                if (!classificationResult) {
                    System.out.println("\t\t[PreprocessService] (AI) 마약 관련 홍보글이 아닙니다!");
                } else {
                    System.out.println("\t\t[PreprocessService] (AI) 마약 관련 홍보글입니다!");
                    String savedId = saveData(html, url, title, source, content, telegrams); // 저장
                    System.out.println("\t\t[PreprocessService] (AI) " + url + " saved");

                    getChannelInfo(telegrams, savedId);
                }
            }

        } catch (Exception e) {
            System.out.println("\t\t[PreprocessService] (AI) HTML 전처리 중 오류 발생: " + e.getMessage());
        }
    }
}
