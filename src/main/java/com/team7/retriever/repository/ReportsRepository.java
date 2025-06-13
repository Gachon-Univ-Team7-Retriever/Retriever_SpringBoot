package com.team7.retriever.repository;

import com.team7.retriever.entity.Reports;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ReportsRepository extends MongoRepository<Reports, String> {

    // 채널 아이디로 조회
    List<Reports> findByChannelId(long channelId);

    // type에 포함
    @Query("{ 'type':  { $regex: ?0, $options: 'i' } }")
    List<Reports> findByType(String type);

    // content에 포함
    @Query("{ 'content':  { $regex: ?0, $options: 'i' } }")
    List<Reports> findByContent(String content);

    // description에 포함
    @Query("{ 'description':  { $regex: ?0, $options: 'i' } }")
    List<Reports> findByDescription(String description);

}
