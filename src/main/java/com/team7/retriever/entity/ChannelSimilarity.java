package com.team7.retriever.entity;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;
import java.util.List;

@Document(collection = "channel_similarity")
public class ChannelSimilarity {
    @Id
    private String id;
    private String channelId;
    private List<SimilarChannel> similarChannels;
    private LocalDateTime updatedAt;

    public static class SimilarChannel {
        private String similarChannel;
        private Double similarity;

        public String getSimilarChannel() {
            return similarChannel;
        }

        public void setSimilarChannel(String similarChannel) {
            this.similarChannel = similarChannel;
        }

        public Double getSimilarity() {
            return similarity;
        }

        public void setSimilarity(Double similarity) {
            this.similarity = similarity;
        }
    }

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

    public List<SimilarChannel> getSimilarChannels() {
        return similarChannels;
    }

    public void setSimilarChannels(List<SimilarChannel> similarChannels) {
        this.similarChannels = similarChannels;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }
}
