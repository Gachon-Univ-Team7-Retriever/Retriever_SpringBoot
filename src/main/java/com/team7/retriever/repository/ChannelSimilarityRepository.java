package com.team7.retriever.repository;

import com.team7.retriever.entity.ChannelSimilarity;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ChannelSimilarityRepository extends MongoRepository<ChannelSimilarity, String> {
    ChannelSimilarity findByChannelId(long channelId);
}