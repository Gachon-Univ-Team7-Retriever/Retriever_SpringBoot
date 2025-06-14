package com.team7.retriever.neo4j.repository;

import com.team7.retriever.neo4j.entity.Channel;
import org.springframework.data.neo4j.repository.Neo4jRepository;

import java.util.Optional;


public interface NeoChannelRepository extends Neo4jRepository<Channel, Long> {

    Optional<Channel> findById(Long channelId);

}

