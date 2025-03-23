package com.team7.retriever.controller;

import com.team7.retriever.dto.PreprocessRequest;
import com.team7.retriever.service.PreprocessService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/html")
public class PreprocessController {
    @Autowired
    private PreprocessService preprocessService;

    @PostMapping("/preprocess")
    public String htmlPreprocess(@RequestBody PreprocessRequest preprocessRequest) {
        String url = preprocessRequest.getUrl();
        String requestData = preprocessRequest.getHtml();

        return preprocessService.postPreprocess(url, requestData);
    }
}
