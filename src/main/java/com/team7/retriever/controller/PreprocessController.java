package com.team7.retriever.controller;

import com.team7.retriever.dto.PreprocessRequest;
import com.team7.retriever.service.PreprocessService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/preprocess")
public class PreprocessController {
    @Autowired
    private PreprocessService preprocessService;

    @GetMapping("/extract-domain")
    public String extractDomain(@RequestParam String url) {
        return preprocessService.extractDomain(url);
    }

    // 아래는 직접 실행하는 코드 (업데이트X)
    /*
    @PostMapping("/preprocess")
    public String htmlPreprocess(@RequestBody PreprocessRequest preprocessRequest) {
        String url = preprocessRequest.getUrl();
        String requestData = preprocessRequest.getHtml();

        return preprocessService.postPreprocess(url, requestData);
    }

     */
}
