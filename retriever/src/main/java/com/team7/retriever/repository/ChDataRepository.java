package com.team7.retriever.repository;

import com.team7.retriever.entity.ChData;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ChDataRepository extends MongoRepository<ChData, String> {
    
    // 유저 아이디로 조회
    List<ChData> findByUserId(String userId);
    
    // 채널 아이디로 조회
    List<ChData> findByChannelId(String channelId);
    
    // 메시지 url로 조회
    List<ChData> findByMsgUrl(String msgUrl);
}

