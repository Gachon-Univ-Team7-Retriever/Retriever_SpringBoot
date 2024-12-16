package com.team7.retriever.entity;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Document(collection = "bookmarks")
public class Bookmarks {

    @Id
    private String id;
    private String channelId;
    private String userId;
    private LocalDateTime createdAt;

    // Getters & Setters
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getChannelId() {
        return channelId;
    }

    public void setChannelId(String channelId) {
        this.channelId = channelId;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    @Override
    public String toString() {
        return "Bookmark{" +
                "id='" + id + '\'' +
                ", channelId='" + channelId + '\'' +
                ", userId='" + userId + '\'' +
                ", createdAt=" + createdAt +
                '}';
    }

    public void setDefaultValues() {
        this.createdAt = LocalDateTime.now();  // 현재 시간으로 설정
        this.id = "bm_"+userId+"_"+channelId;
    }
}
