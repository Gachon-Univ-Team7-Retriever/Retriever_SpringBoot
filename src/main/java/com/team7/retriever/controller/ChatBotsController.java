package com.team7.retriever.controller;

import com.team7.retriever.entity.ChatBots;
import com.team7.retriever.service.ChatBotsService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@AllArgsConstructor
@RequestMapping("/chatbots")
public class ChatBotsController {

    private final ChatBotsService chatBotsService;

    // 전체 조회
    @GetMapping("/all")
    public List<ChatBots> getAllChatBots() {
        return chatBotsService.getAllChatBots();
    }

    // 아이디로 조회
    @GetMapping("/id/{id}")
    public Optional<ChatBots> getChatBotsById(@PathVariable long id) {
        return chatBotsService.getChatBotsById(id);
    }

    // 채널 아이디로 조회
    @GetMapping("/channels")
    public List<ChatBots> getChatBotsByChannels(@RequestParam List<Long> channelIds) {
        return chatBotsService.getChatBotsByChannels(channelIds);
    }
}
