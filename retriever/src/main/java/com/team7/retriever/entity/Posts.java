package com.team7.retriever.entity;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import java.time.LocalDateTime;

@Document(collection = "posts")
public class Posts {

    @Id
    private String id;
    private String link;
    private String tag;
    private String siteName;
    private String title;
    private String content;
    private String promoSiteLink;
    private String promoSiteName;
    private String author;
    private LocalDateTime timestamp;
    private LocalDateTime createdAt;

    public Posts() {}

    // Getters & Setters
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }

    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public String getSiteName() {
        return siteName;
    }

    public void setSiteName(String siteName) {
        this.siteName = siteName;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getPromoSiteLink() {
        return promoSiteLink;
    }

    public void setPromoSiteLink(String promoSiteLink) {
        this.promoSiteLink = promoSiteLink;
    }

    public String getPromoSiteName() {
        return promoSiteName;
    }

    public void setPromoSiteName(String promoSiteName) {
        this.promoSiteName = promoSiteName;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }
}
