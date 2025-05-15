package com.team7.retriever.repository;

import com.team7.retriever.entity.ChInfo;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ChInfoRepository extends MongoRepository<ChInfo, String> {

    Optional<ChInfo> findById(long id);
    
    // 채널 링크로 조회
    Optional<ChInfo> findByLink(String link);

    /* 250102 추가 */
    // 채널 이름에 포함 (대소문자 무시)
    @Query("{ 'title': { $regex: ?0, $options: 'i' } }")
    List<ChInfo> findByTitleContaining(String title);

    boolean existsById(String id);
}