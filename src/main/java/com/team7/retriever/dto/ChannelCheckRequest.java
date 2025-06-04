package com.team7.retriever.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Builder
public class ChannelCheckRequest {
    @JsonProperty("channel_name")
    private String channel;
}
