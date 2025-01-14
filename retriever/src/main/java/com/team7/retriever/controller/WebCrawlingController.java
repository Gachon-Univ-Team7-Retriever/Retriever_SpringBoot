package com.team7.retriever.controller;

import com.team7.retriever.dto.WebCrawlingRequest;
import com.team7.retriever.dto.WebCrawlingResponse;
import com.team7.retriever.service.WebCrawlingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/webcrawl")
public class WebCrawlingController {
    @Autowired
    private WebCrawlingService webCrawlingService;

    /*
    // 기존 모듈 컨트롤러
    @GetMapping("/{keyword}")
    public List<Map<String, Object>> getCrawlResults(@PathVariable String keyword) {
        return webCrawlingService.webCrawling(keyword);
        // return "Crawl results printed to console.";
    }
     */

    // 250108 추가
    @PostMapping()
    public WebCrawlingResponse crawlWebCrawling(@RequestBody WebCrawlingRequest request) {
        return webCrawlingService.webCrawling(request);
    }
}
