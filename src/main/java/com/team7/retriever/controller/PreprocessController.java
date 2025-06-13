package com.team7.retriever.controller;

import com.team7.retriever.service.PreprocessService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;

@RestController
@AllArgsConstructor
@RequestMapping("/preprocess")
public class PreprocessController {
    private final PreprocessService preprocessService;

    @GetMapping("/extract-domain")
    public String extractDomain(@RequestParam String url) {
        return preprocessService.extractDomain(url);
    }
}
