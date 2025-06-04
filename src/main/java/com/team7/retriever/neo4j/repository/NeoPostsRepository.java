package com.team7.retriever.neo4j.repository;


import com.team7.retriever.neo4j.entity.Posts;
import org.springframework.data.neo4j.repository.Neo4jRepository;

import java.util.Optional;

public interface NeoPostsRepository extends Neo4jRepository<Posts, String> {

    Optional<Posts> findByPostId(String postId);

}
