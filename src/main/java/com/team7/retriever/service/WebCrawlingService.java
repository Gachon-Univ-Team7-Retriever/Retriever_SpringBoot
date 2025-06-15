package com.team7.retriever.service;

// import com.team7.retriever.dto.CrawlGoogleResponse;
import com.team7.retriever.dto.SerpApiCrawlingResponse;
import com.team7.retriever.dto.WebCrawlingRequest;
import com.team7.retriever.dto.WebCrawlingResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

/*
    @Service(스프링 빈에 등록된 클래스) 라서
    어노테이션 내부에 이미 @Component가 포함되어 있기 때문에
    @Component는 따로 추가하지 않아도 된다 고 한다
( @Component는 스케줄러를 적용할 대상 클래스에 추가하는 것임 )
*/
@Service
@Slf4j
@RequiredArgsConstructor
public class WebCrawlingService {
    private final RestTemplate restTemplate;
    private final HtmlCrawlingService htmlCrawlingService;
    private final PreprocessService preprocessService;
    private final PostHtmlService postHtmlService;
    private final ChInfoService chInfoService;
    private final ArgotsService argotsService;
    private final PostSimilarityService postSimilarityService;
    private final ChannelInfoService channelInfoService;
    private final UpdateCheckService updateCheckService;

    @Scheduled(cron = "0 0 5 * * SUN") // 매주 일요일 오전 5시 실행 -> 기존 데이터 업데이트 체크하는 메서드 끝나면 새로운 데이터 수집 실행
    public void sundayJob() {
        log.info("[SunDayJob] UpdateCheckService 실행 시작");
        updateCheckService.updateAllPost();
        log.info("[SunDayJob] UpdateCheckService 실행 완료");

        log.info("[SunDayJob] WebCrawlingService 실행 시작");
        // webCrawling();
        webCrawlingSerpApi();
        log.info("[SunDayJob] WebCrawlingService 실행 완료");
    }

    // 초(0-59) 분(0-59) 시간(0-23) 일(1-31) 월(1-12) 요일(0-6) (0: 일, 1: 월, 2:화, 3:수, 4:목, 5:금, 6:토)
    // initialDelay = 5000 -> 초기 5초 지연 시간 설정 -> 스케줄 안에 같이 넣는 것 (참고 용으로 기록)
    // @Scheduled(fixedDelay = 120000) // 테스트 용 - 한 사이클 종료 후 2분 지연 실행
    // @Scheduled(cron = "0 0 5 * * *") // 매일 오전 5시마다 실행
    @Scheduled(cron = "0 0 5 * * MON-SAT") // 매주 월-토 오전 5시마다 실행
    public void webCrawling() {
        String api = "http://127.0.0.1:5050/crawl/links";

        WebCrawlingRequest webCrawlingRequest = new WebCrawlingRequest();
        webCrawlingRequest.setQueries(argotsService.getAllArgotsToListWtme());
        webCrawlingRequest.setMax(5);

        HttpEntity<WebCrawlingRequest> request = new HttpEntity<>(webCrawlingRequest);
        ResponseEntity<WebCrawlingResponse> response = restTemplate.postForEntity(api, request, WebCrawlingResponse.class);

        WebCrawlingResponse results = response.getBody();
        if (results != null) {
            List<String> google = results.getGoogle();
            List<String> telegram = results.getTelegrams();

            // int inserted = 0;
            // int updated = 0;

            // google
            log.info("[WebCrawlingService] Google 결과 시작");
            if (google != null) {
                for (String googleResponse : google) {
                    log.info("- " + googleResponse);
                    // 해당 링크가 DB에 있는지 체크
                    if (postHtmlService.isUrlExists(googleResponse)) { // DB에 이미 존재하면 skip
                        log.info("[WebCrawlingService] DB에 해당 게시물이 이미 존재합니다 !");
                    } else { // DB에 존재하지 않으면 html 크롤링 시작
                        // 홍보글 내용 추출
                        String html = htmlCrawlingService.crawlHtml(googleResponse); // 크롤링 결과 받아옴
                        if (html != null) {
                            log.info("[WebCrawlingService] 내용 추출 완료");
                            // System.out.println("\t\t- " + html);
                            // log.debug("\t\t- " + html);
                            // preprocessService.htmlPreprocess(googleResponse, null, null, html); // 전처리 실행
                            preprocessService.htmlPreprocessAi(googleResponse, null, null, html); // AI 사용 전처리 실행
                            log.info("[WebCrawlingService] 전처리 모듈 실행 완료");
                        } else {
                            log.error("[WebCrawlingService] 내용 추출 실패");
                        }
                    }
                    log.info("[WebCrawlingService] 크롤링 실행 완료");

                    // 유사도 모듈 실행 서비스
                    log.info("[WebCrawlingService] 유사도 모듈 호출");
                    postSimilarityService.calculateSimilarity();
                    log.info("[WebCrawlingService] 실행 완료");
                }
            } else {
                log.warn("[WebCrawlingService] No google found");
            }

            // telegram
            log.info("[WebCrawlingService] Telegrams 결과 시작");
            if (telegram != null) {
                for (String telegramResponse : telegram) {
                    log.info("\t- " + telegramResponse);
                    if (chInfoService.isChannelExists(telegramResponse)) { // DB에 이미 정보가 존재하면 스킵
                        log.info("[WebCrawlingService] DB에 해당 채널이 이미 존재합니다 !");
                    } else { // DB에 해당 채널 아이디가 존재하지 않으면 채널 검문 모듈 실행
                        log.info("[WebCrawlingService] 채널 정보 수집 요청");
                        channelInfoService.getChannelInfo(telegramResponse, null);
                        log.info("[WebCrawlingService] 채널 정보 수집 완료");
                    }
                }
            } else {
                log.warn("[WebCrawlingService] No telegram found");
            }
            log.info("[WebCrawlingService] 모든 결과에 대한 처리 완료");
        }

    }

    // SeapAPI Web Link Crawling
    @Scheduled(cron = "0 0 5 * * MON-SAT") // 매주 월-토 오전 5시마다 실행
    public void webCrawlingSerpApi() {
        String baseApi = "http://127.0.0.1:5050/crawl/links/serpapi";

        List<String> argotList = argotsService.getAllArgotsToList();
        int max_results = 3;

        StringBuilder queryStringBuilder = new StringBuilder();
        for (String argot : argotList) {
            String rawQuery = "t.me " + argot;
            queryStringBuilder.append("q=").append(rawQuery).append("&");
        }
        /*
        for (String argot : argotList) {
            String rawQuery = "텔레 " + argot;
            queryStringBuilder.append("q=").append(rawQuery).append("&");
        }
        */
        /*
        for (String argot : argotList) {
            String rawQuery = argot + " 팝니다";
            queryStringBuilder.append("q=").append(rawQuery).append("&");
        }
        */

        queryStringBuilder.append("max_results=").append(max_results);

        String finalQueryString = queryStringBuilder.toString();
        String API = baseApi + "?" + finalQueryString;

        log.info("[WebCrawlingSerpApi] API: " + API);


        ResponseEntity<SerpApiCrawlingResponse> response = restTemplate.getForEntity(API, SerpApiCrawlingResponse.class);

        SerpApiCrawlingResponse results = response.getBody();

        if (results != null) {
            List<SerpApiCrawlingResponse.CrawlRes> googleRes = results.getGoogle();
            List<String> telegrams = results.getTelegrams();


            // google
            log.info("[WebCrawlingService] Google 결과 시작");
            if (googleRes != null) {
                for (SerpApiCrawlingResponse.CrawlRes res : googleRes) {
                    log.info("- " + res.getLink());
                    log.info("\t- " + res.getTitle());
                    log.info("\t- " + res.getSource());
                    // res.getLink(), res.getTitle(), res.getSource()
                    // 해당 링크가 DB에 있는지 체크
                    if (postHtmlService.isUrlExists(res.getLink())) { // DB에 이미 존재하면 skip
                        log.info("[WebCrawlingService] DB에 해당 게시물이 이미 존재합니다 !");
                    } else { // DB에 존재하지 않으면 html 크롤링 시작
                        // 홍보글 내용 추출
                        String html = htmlCrawlingService.crawlHtml(res.getLink()); // 크롤링 결과 받아옴
                        if (html != null) {
                            log.info("[WebCrawlingService] HTML 추출 완료");
                            // System.out.println("\t\t- " + html);
                            // log.debug("\t\t- " + html);
                            // preprocessService.htmlPreprocess(res.getLink(), res.getTitle(), res.getSource(), html); // 전처리 실행
                            preprocessService.htmlPreprocessAi(res.getLink(), res.getTitle(), res.getSource(), html);
                            log.info("[WebCrawlingService] 전처리 모듈 실행 완료");
                        } else {
                            log.error("[WebCrawlingService] 내용 추출 실패");
                        }
                    }
                    log.info("[WebCrawlingService] 크롤링 실행 완료");

                }
                log.info("[WebCrawlingService] Google 처리 완료");
                // 유사도 모듈 실행 서비스
                log.info("[WebCrawlingService] 유사도 모듈 호출");
                postSimilarityService.calculateSimilarity();
                log.info("[WebCrawlingService] 실행 완료");

            } else {
                log.warn("[WebCrawlingService] No google found");
            }

            // telegrams
            log.info("[WebCrawlingService] Telegrams 결과 시작");
            if (telegrams != null) {
                for (String telegram : telegrams) {
                    log.info("\t- " + telegram);
                    if (chInfoService.isChannelExists(telegram)) { // DB에 이미 정보가 존재하면 스킵
                        log.info("[WebCrawlingService] DB에 해당 채널이 이미 존재합니다 !");
                    } else { // DB에 해당 채널 아이디가 존재하지 않으면 채널 검문 모듈 실행
                        log.info("[WebCrawlingService] 채널 정보 수집 요청");
                        channelInfoService.getChannelInfo(telegram, null);
                        log.info("[WebCrawlingService] 채널 정보 수집 완료");
                    }
                }
                log.info("[WebCrawlingService] Telegrams 처리 완료");
            } else {
                log.warn("[WebCrawlingService] No telegram found");
            }
            log.info("[WebCrawlingService] 모든 결과에 대한 처리 완료");
        }

    }

}
