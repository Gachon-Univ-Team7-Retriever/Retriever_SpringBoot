package com.team7.retriever.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Getter
@Setter
@Builder
public class PreprocessResponse {
    private Boolean classificationResult;
    private String promotionContent;
    private List<String> telegrams;
}
