package com.team7.retriever.neo4j.dto;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class PromotionRequest {
    private Long channelId;
    private String postId;
}
