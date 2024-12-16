package com.team7.retriever.service;


import com.team7.retriever.entity.ChInfo;
import com.team7.retriever.repository.ChInfoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
public class ChInfoService {
    @Autowired
    private final ChInfoRepository chInfoRepository;

    public ChInfoService(ChInfoRepository chInfoRepository) {
        this.chInfoRepository = chInfoRepository;
    }

    // test code
    public void addChInfo (String id, String name, String link, String desc, LocalDateTime createdAt, LocalDateTime updatedAt, LocalDateTime deletedAt) {
        ChInfo chInfo = new ChInfo(id, name, link, desc, createdAt, updatedAt, deletedAt);
        // 위 코드를 setter 쓰는 걸로 수정하면 됨
        // addChInfo 자체에 들어있는 파라미터도 삭제하고, 읽어온 데이터로 대체하면 됨
        // 데이터 한 줄씩 돌면서 세이브 해주면 될 듯
        chInfoRepository.save(chInfo);
    }

    // 모든 채널 정보 조회
    public List<ChInfo> getAllChannelInfo() {
        return chInfoRepository.findAll();
    }

    // 채널 아이디로 해당 채널 조회
    public Optional<ChInfo> getChannelInfoById(String id) {
        return chInfoRepository.findById(id);
    }

    // 채널 링크로 해당 채널 조회
    public Optional<ChInfo> getChannelByLink(String link) {
        return chInfoRepository.findByLink(link);
    }
}
