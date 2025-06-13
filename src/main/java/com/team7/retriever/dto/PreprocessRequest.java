package com.team7.retriever.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class PreprocessRequest {
    private String url;
    private String html;

}
