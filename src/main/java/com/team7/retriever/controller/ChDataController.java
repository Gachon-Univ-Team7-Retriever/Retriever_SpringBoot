package com.team7.retriever.controller;

import com.team7.retriever.dto.ChatArgotDrugDTO;
import com.team7.retriever.entity.ChData;
import com.team7.retriever.service.ChDataService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("/chat")
public class ChDataController {

    private final ChDataService chDataService;

    // 전체 채팅 조회
    @GetMapping("/all")
    public List<ChData> getAllChannelData() {
        return chDataService.getAllChannelData();
    }

    // 채널 아이디로 채팅 조회
    @GetMapping("/channel/{channelID}")
    public List<ChData> getChannelDataByChannelId(@PathVariable long channelID) {
        return chDataService.getChannelDataByChannelId(channelID);
    }

    // 유저 아이디로 채팅 조회
    @GetMapping("/user/id/{senderID}")
    public List<ChData> getChannelDataBySenderId(@PathVariable long senderID) {
        return chDataService.getChannelDataBySenderId(senderID);
    }

    // 유저 이름으로 채팅 조회
    @GetMapping("/user/name/{senderName}")
    public List<ChData> getChannelDataBySenderName(@PathVariable String senderName) {
        return chDataService.getChannelDataBySederName(senderName);
    }

    // 메시지 url로 채팅 조회
    @GetMapping("/by-msg-url")
    public List<ChData> getChannelDataByMsgUrl(@RequestParam String msgUrl) {
        return chDataService.getChannelDataByUrl(msgUrl);
    }

    // 채팅 내용에 포함
    @GetMapping("/text")
    public List<ChData> getChannelDataByText(@RequestParam String text) {
        return chDataService.getChannelDataByText(text);
    }

    // argot & drugs data
    @GetMapping("/data")
    public List<ChatArgotDrugDTO> getArgotDrugsData() {
        return chDataService.getArgotDrugsData();
    }
}
