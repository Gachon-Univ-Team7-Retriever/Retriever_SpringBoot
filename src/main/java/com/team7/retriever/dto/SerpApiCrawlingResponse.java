package com.team7.retriever.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
@Builder
public class SerpApiCrawlingResponse {

    private List<CrawlRes> google;
    private List<String> telegrams;

    @Getter
    @Setter
    @Builder
    public static class CrawlRes {
        private String link;
        private String title;
        private String source;
    }
}
