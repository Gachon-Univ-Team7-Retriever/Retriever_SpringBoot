package com.team7.retriever.controller;

import com.team7.retriever.dto.WebCrawlingResponse;
import com.team7.retriever.service.ArgotsService;
import com.team7.retriever.service.UpdateCheckService;
import com.team7.retriever.service.WebCrawlingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/webcrawl")
public class WebCrawlingController {
    @Autowired
    private WebCrawlingService webCrawlingService;
    @Autowired
    private ArgotsService slangsService;
    @Autowired
    private UpdateCheckService updateCheckService;

    /*
    // 기존 모듈 컨트롤러
    @GetMapping("/{keyword}")
    public List<Map<String, Object>> getCrawlResults(@PathVariable String keyword) {
        return webCrawlingService.webCrawling(keyword);
        // return "Crawl results printed to console.";
    }
     */

    // DB에서 데이터 받아서 실행
    @PostMapping()
    public WebCrawlingResponse webCrawling() {
        return webCrawlingService.webCrawling();
    }

    // DB에서 데이터 조회 결과 테스트
    @GetMapping("/slangs")
    public List<String> getSlangs() {
        return slangsService.getAllArgotsToList();
    }

    // DB 데이터 업데이트 사항 확인
    @GetMapping("/updates")
    public void updateCheck() {
        updateCheckService.getAllPost();
    }

    /*
    // 250123 수정
    // 클라이언트가 바디 세팅
    @PostMapping("/test")
    public WebCrawlingResponse webCrawlingTest(@RequestBody WebCrawlingRequest request) {
        return webCrawlingService.webCrawlingTest(request);
    }

     */
}
