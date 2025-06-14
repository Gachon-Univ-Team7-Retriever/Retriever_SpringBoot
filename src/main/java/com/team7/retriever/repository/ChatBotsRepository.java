package com.team7.retriever.repository;

import com.team7.retriever.entity.ChatBots;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ChatBotsRepository extends MongoRepository<ChatBots, String> {
    // id
    Optional<ChatBots> findById(long id);

    // channels
    List<ChatBots> findByChannelsIn(List<Long> channelIds);
}