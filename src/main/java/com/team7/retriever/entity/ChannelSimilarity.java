package com.team7.retriever.entity;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;
import java.util.List;

@Getter
@Setter
@Document(collection = "channel_similarity")
public class ChannelSimilarity {
    @Id
    private String id;
    private String channelId;
    private List<SimilarChannel> similarChannels;
    private LocalDateTime updatedAt;

    @Getter
    public static class SimilarChannel {
        private String similarChannel;
        private Double similarity;
    }

}
