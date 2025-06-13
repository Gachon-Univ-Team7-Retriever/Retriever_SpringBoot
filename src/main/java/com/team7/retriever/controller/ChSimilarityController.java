package com.team7.retriever.controller;

import com.team7.retriever.entity.ChannelSimilarity;
import com.team7.retriever.service.ChSimilarityService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("channel-similarity")
public class ChSimilarityController {

    private final ChSimilarityService chSimilarityService;

    @GetMapping("/all")
    public List<ChannelSimilarity> getAllChannelSimilarity() {
        return chSimilarityService.getAllChannelSimilarity();
    }

    @GetMapping("/id/{id}")
    public ChannelSimilarity getChannelSimilarityById(@PathVariable String id) {
        return chSimilarityService.getChannelSimilarityById(id);
    }

    @GetMapping("/chId/{channelId}")
    public ChannelSimilarity getChannelSimilarityByChannelId(@PathVariable long channelId) {
        return chSimilarityService.getChannelSimilarityByChannelId(channelId);
    }
}
