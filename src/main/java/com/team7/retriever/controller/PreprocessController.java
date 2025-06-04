package com.team7.retriever.controller;

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
}
