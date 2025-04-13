package com.team7.retriever.entity;

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
    // private String promoSiteLink;
    // private String promoSiteName;
    private List<String> promoSiteLink;
    private List<String> promoChannelId; // promoSiteName -> promoChannelId
    private String author;
    private LocalDateTime timestamp;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private LocalDateTime deletedAt;
    private boolean deleted;

}
