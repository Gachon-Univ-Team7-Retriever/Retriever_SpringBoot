package com.team7.retriever.repository;

import com.team7.retriever.entity.ChInfo;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface ChInfoRepository extends MongoRepository<ChInfo, String> {
    
    // 채널 링크로 조회
    Optional<ChInfo> findByLink(String link);
}