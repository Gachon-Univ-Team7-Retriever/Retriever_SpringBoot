package com.team7.retriever.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Getter
@Setter
@NoArgsConstructor
@Document(collection = "post_html")
public class PostHtml {

    @Id
    private String id;
    private String postId;
    private String html;
    private String url; /* 250102 추가 */
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    @Builder
    public PostHtml(String postId, String html, String url, LocalDateTime createdAt, LocalDateTime updatedAt) {
        this.postId = postId;
        this.html = html;
        this.url = url;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }
}
