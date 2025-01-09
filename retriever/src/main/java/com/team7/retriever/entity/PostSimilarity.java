package com.team7.retriever.entity;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;
import java.util.List;

@Document(collection = "post_similarity")
public class PostSimilarity {

    @Id
    private String id;
    private String postId;
    private List<SimilarPost> similarPosts;
    private LocalDateTime updatedAt;

    // Inner class for similar posts (게시글 간 유사도 배열)
    public static class SimilarPost {
        private String similarPost;
        private double similarity;

        // Getters & Setters
        public String getSimilarPost() {
            return similarPost;
        }

        public void setSimilarPost(String similarPost) {
            this.similarPost = similarPost;
        }

        public double getSimilarity() {
            return similarity;
        }

        public void setSimilarity(double similarity) {
            this.similarity = similarity;
        }
    }

    // Getters & Setters
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getPostId() {
        return postId;
    }

    public void setPostId(String postId) {
        this.postId = postId;
    }

    public List<SimilarPost> getSimilarPosts() {
        return similarPosts;
    }

    public void setSimilarPosts(List<SimilarPost> similarPosts) {
        this.similarPosts = similarPosts;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }
}
