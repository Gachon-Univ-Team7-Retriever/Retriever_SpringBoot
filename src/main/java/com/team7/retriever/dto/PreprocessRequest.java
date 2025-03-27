package com.team7.retriever.dto;

public class PreprocessRequest {
    private String url;
    private String html;

    // Getter & Setter
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getHtml() {
        return html;
    }

    public void setHtml(String html) {
        this.html = html;
    }
}
