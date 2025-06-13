package com.team7.retriever.service;

import com.team7.retriever.dto.UpdateCheckRequest;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service
@RequiredArgsConstructor
public class UpdateCheckService {
    private final PostsService postsService;
    private final HtmlCrawlingService htmlCrawlingService;
    private final PreprocessService preprocessService;
    private final PostSimilarityService postSimilarityService;

    public void updateAllPost() {
        List<UpdateCheckRequest> allPosts = postsService.getAllPostsForUpdate();

        for (UpdateCheckRequest post : allPosts) {
            updatePost(post);
        }
    }

    public void updatePost(UpdateCheckRequest post) {
        String link = post.link();
        String title = post.title();
        String source = post.source();

        log.info("[UpDateCheckService] 크롤링 시작 / link: " + link);
        String newHtml = htmlCrawlingService.crawlHtml(link);
        if (newHtml != null) {
            log.info("[UpDateCheckService] 내용 추출 완료");
            preprocessService.updatePreprocess(newHtml, link, title, source);
            log.info("[UpDateCheckService] 실행 완료");

            // 유사도 모듈 실행 서비스
            log.info("[WebCrawlingService] 유사도 모듈 호출");
            postSimilarityService.calculateSimilarity();
            log.info("[WebCrawlingService] 실행 완료");
        } else {
            log.info("[UpDateCheckService] HTML 크롤링 결과 없음");
        }
    }
}
