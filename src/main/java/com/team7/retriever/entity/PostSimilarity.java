package com.team7.retriever.entity;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;
import java.util.List;

@Getter
@Setter
@Document(collection = "post_similarity")
public class PostSimilarity {

    @Id
    private String id;
    private String postId;
    private List<SimilarPost> similarPosts;
    private LocalDateTime updatedAt;

    // Inner class for similar posts (게시글 간 유사도 배열)
    @Getter
    public static class SimilarPost {
        private String similarPost;
        private double similarity;
    }

}
