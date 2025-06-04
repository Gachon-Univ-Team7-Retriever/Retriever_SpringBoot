package com.team7.retriever.dto;

import lombok.Getter;

import java.util.List;

@Getter
public class WebCrawlingResponse {
    // private List<CrawlGoogleResponse> google;
    private List<String> google;
    private List<String> telegrams;
}
