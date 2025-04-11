package com.team7.retriever.controller;

import com.team7.retriever.service.ChannelInfoService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/channelInfo")
public class ChannelInfoController {
    private final ChannelInfoService channelInfoService;

    public ChannelInfoController(ChannelInfoService channelInfoService) {
        this.channelInfoService = channelInfoService;
    }

    @GetMapping
    public void getChannelInfo(@RequestParam String token) {
        channelInfoService.getChannelInfo(token);
    }
}
