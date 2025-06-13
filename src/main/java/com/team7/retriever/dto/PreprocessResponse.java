package com.team7.retriever.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
@Builder
public class PreprocessResponse {
    @JsonProperty("classification_result")
    private Boolean classificationResult;
    @JsonProperty("promotion_content")
    private String promotionContent;
    private List<String> telegrams;
}
