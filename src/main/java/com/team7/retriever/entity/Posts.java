package com.team7.retriever.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import java.time.LocalDateTime;
import java.util.List;

@Getter
@Setter
@Builder
@Document(collection = "posts")
public class Posts {

    @Id
    private String id;
    private String link;
    private String tag;
    private String siteName;
    private String title;
    private String content;
    private String source;
    private List<String> promoSiteLink;
    private List<String> promoChannelId; // promoSiteName -> promoChannelId
    private String author;
    private LocalDateTime timestamp;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private LocalDateTime deletedAt;
    private boolean deleted;

    public void updateTimestampToNow() {
        this.updatedAt = LocalDateTime.now();
    }

    public void markAsDeleted(LocalDateTime timestamp) {
        this.deleted = true;
        this.deletedAt = timestamp;
        this.updatedAt = timestamp;
    }

}
