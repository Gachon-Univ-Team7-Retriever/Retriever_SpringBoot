package com.team7.retriever.controller;

import com.team7.retriever.service.ArgotsService;
import com.team7.retriever.service.UpdateCheckService;
import com.team7.retriever.service.WebCrawlingService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("/webcrawl")
public class WebCrawlingController {
    private final WebCrawlingService webCrawlingService;
    private final ArgotsService argotsService;
    private final UpdateCheckService updateCheckService;

    // DB에서 데이터 받아서 실행
    // 기존 웹크롤링
    @GetMapping()
    public void webCrawling() {
        webCrawlingService.webCrawling();
    }

    // DB에서 데이터 받아서 실행
    // SerpAPI
    @GetMapping
    public void webCrawlSerp() {
        webCrawlingService.webCrawlingSerpApi();
    }

    // DB에서 데이터 조회 결과 테스트
    @GetMapping("/argots")
    public List<String> getArgots() {
        return argotsService.getAllArgotsToList();
    }

    // DB 데이터 업데이트 사항 확인
    @GetMapping("/updates")
    public void updateCheck() {
        updateCheckService.updateAllPost();
    }

}
