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


    @Builder
    public Posts(String link, String tag, String siteName, String title, String content,
                 List<String> promoSiteLink, List<String> promoChannelId, String author,
                 LocalDateTime timestamp, LocalDateTime createdAt, LocalDateTime updatedAt,
                 LocalDateTime deletedAt, boolean deleted) {
        this.link = link;
        this.tag = tag;
        this.siteName = siteName;
        this.title = title;
        this.content = content;
        this.promoSiteLink = promoSiteLink;
        this.promoChannelId = promoChannelId;
        this.author = author;
        this.timestamp = timestamp;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
        this.deletedAt = deletedAt;
        this.deleted = deleted;
    }

    public void updateTimestampToNow() {
        this.updatedAt = LocalDateTime.now();
    }

    public void markAsDeleted(LocalDateTime timestamp) {
        this.deleted = true;
        this.deletedAt = timestamp;
        this.updatedAt = timestamp;
    }

}
