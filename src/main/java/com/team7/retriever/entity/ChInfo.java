package com.team7.retriever.entity;

import lombok.Getter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import java.time.LocalDateTime;
import java.util.List;

@Getter
@Document(collection = "channel_info")
public class ChInfo {
    @Id
    private Long id;
    private String title;
    private String username;
    private Boolean restricted;
    private String link; // -> 초대코드로 변경
    private String description; // 모듈에서 저장 없음
    private LocalDateTime startedAt;
    @Field("discoveredAt")
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private LocalDateTime deletedAt;
    private LocalDateTime chatbotUpdatedAt;
    private int promoCount; // 일단 보류
    private String status;
    private Catalog catalog;

    @Getter
    public static class Catalog {
        @Field("chatIds")
        private List<Integer> chatIds;
        private String description;
    }

}
