package com.team7.retriever.repository;

import com.team7.retriever.entity.Bookmarks;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BookmarksRepository extends MongoRepository<Bookmarks, String> {
    
    // 유저 아이디로 조회
    List<Bookmarks> findByUserId(String userId);
}
