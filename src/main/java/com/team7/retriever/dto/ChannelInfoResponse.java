package com.team7.retriever.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Getter
@NoArgsConstructor
@AllArgsConstructor
public class ChannelInfoResponse {

    private long id;
    private String title;
    private String username;
    private Boolean restricted;
    private LocalDateTime startedAt;
    private LocalDateTime discoveredAt;
    private LocalDateTime updatedAt;
    private String status;

}
