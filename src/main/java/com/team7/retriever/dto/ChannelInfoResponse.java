package com.team7.retriever.dto;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Data
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class ChannelInfoResponse {

    @JsonProperty("_id")
    private Long id;
    private String title;
    private String username;
    private Boolean restricted;

    @JsonFormat(pattern = "EEE, dd MMM yyyy HH:mm:ss z", locale = "en", timezone = "GMT")
    private String startedAt;

    @JsonFormat(pattern = "EEE, dd MMM yyyy HH:mm:ss z", locale = "en", timezone = "GMT")
    private String discoveredAt;

    @JsonFormat(pattern = "EEE, dd MMM yyyy HH:mm:ss z", locale = "en", timezone = "GMT")
    private String updatedAt;

    private String status;

}
