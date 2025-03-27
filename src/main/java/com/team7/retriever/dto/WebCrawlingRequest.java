package com.team7.retriever.dto;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.List;

public class WebCrawlingRequest {
    private List<String> queries;

    @JsonProperty("max_results")
    private int max;

    // Getter & Setter
    public List<String> getQueries() {
        return queries;
    }

    public void setQueries(List<String> queries) {
        this.queries = queries;
    }

    public int getMax_results() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
}
