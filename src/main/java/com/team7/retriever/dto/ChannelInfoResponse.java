package com.team7.retriever.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
@AllArgsConstructor
public class ChannelInfoResponse {

    private Long id;
    private String title;
    private String username;
    private Boolean restricted;
    private String startedAt;
    private String discoveredAt;
    private String updatedAt;
    private String status;

}
