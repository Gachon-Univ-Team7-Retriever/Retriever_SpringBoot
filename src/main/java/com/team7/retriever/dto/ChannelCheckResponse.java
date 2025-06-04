package com.team7.retriever.dto;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class ChannelCheckResponse {
    private String suspicious;
}
