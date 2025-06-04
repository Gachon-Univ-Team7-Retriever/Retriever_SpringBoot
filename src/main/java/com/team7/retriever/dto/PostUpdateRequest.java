package com.team7.retriever.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class PostUpdateRequest {
    private String html;
    private String link;
    private String title;
    private String source;
}
