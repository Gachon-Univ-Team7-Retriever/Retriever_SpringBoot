package com.team7.retriever.entity;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import java.time.LocalDateTime;

@Getter
@Setter
@Document(collection = "bookmarks")
public class Bookmarks {

    @Id
    private String id;
    private String channelId;
    private String userId;
    private LocalDateTime createdAt;

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
