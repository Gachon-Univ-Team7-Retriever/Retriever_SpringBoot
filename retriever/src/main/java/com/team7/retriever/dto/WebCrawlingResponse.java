package com.team7.retriever.dto;

import java.util.List;

public class WebCrawlingResponse {
    // private List<CrawlGoogleResponse> google;
    private List<String> google;
    private List<String> telegram;

    // Getter & Setter
    public List<String> getGoogle() {
        return google;
    }

    public void setGoogle(List<String> google) {
        this.google = google;
    }

    public List<String> getTelegram() {
        return telegram;
    }

    public void setTelegram(List<String> telegram) {
        this.telegram = telegram;
    }
}
