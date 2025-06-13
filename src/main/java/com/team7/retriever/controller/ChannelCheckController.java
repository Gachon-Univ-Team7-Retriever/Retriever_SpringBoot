package com.team7.retriever.controller;

import com.team7.retriever.dto.ChannelInfoResponse;
import com.team7.retriever.service.ChannelInfoService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@AllArgsConstructor
@RequestMapping("telegram/channel/info")
public class ChannelCheckController {
    private final ChannelInfoService channelInfoService;

    @PostMapping
    public ChannelInfoResponse channelInfo(@RequestParam String token, @RequestParam String postId) {
        return channelInfoService.getChannelInfo(token, postId);
    }
}
