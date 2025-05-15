package com.team7.retriever.controller;


import com.team7.retriever.entity.ChInfo;
import com.team7.retriever.service.ChInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/channels")
public class ChInfoController {
    @Autowired
    private ChInfoService infoService;

    // 전체 채널 조회
    @GetMapping("/all")
    public List<ChInfo> getAllChannelInfo() { return infoService.getAllChannelInfo(); }

    // 특정 아이디로 채널 정보 조회
    @GetMapping("/id/{id}") /* 241231 수정 */
    public Optional<ChInfo> getChannelInfoById(@PathVariable long id) {
        return infoService.getChannelInfoById(id);
    }

    // 채널 링크로 채널 정보 조회
    @GetMapping("/by-link/{link}")
    public Optional<ChInfo> getChannelInfoByLink(@PathVariable String link) {
        return infoService.getChannelByLink(link);
    }

    /* 250102 추가 */
    // 채널 이름에 포함되는 것
    @GetMapping("/title/{title}")
    public List<ChInfo> getChannelInfoByTitleContaining(@PathVariable String title) {
        return infoService.getChannelInfoByTitleContaining(title);
    }
}
