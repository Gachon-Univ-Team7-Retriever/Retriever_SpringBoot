package com.team7.retriever.service;

import com.team7.retriever.entity.ChData;
import com.team7.retriever.repository.ChDataRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ChDataService {
    @Autowired
    private ChDataRepository chDataRepository;

    @Autowired
    public ChDataService(ChDataRepository chDataRepository) {
        this.chDataRepository = chDataRepository;
    }

    // 전체 조회
    public List<ChData> getAllChannelData() {
        return chDataRepository.findAll();
    }

    // 유저 아이디로 조회
    public List<ChData> getChannelDataByUserId(String user_id) {
        return chDataRepository.findByUserId(user_id);
    }

    // 채널 아이디로 조회
    public List<ChData> getChannelDataByChannelId(String channel_id) {
        return chDataRepository.findByChannelId(channel_id);
    }

    // 메시지 url로 조회
    public List<ChData> getChannelDataByMsgUrl(String msgUrl) {
        return chDataRepository.findByMsgUrl(msgUrl);
    }
}
