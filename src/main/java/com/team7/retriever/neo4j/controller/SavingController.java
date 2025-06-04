package com.team7.retriever.neo4j.controller;

import com.team7.retriever.neo4j.dto.PromotionRequest;
import com.team7.retriever.neo4j.service.SavingPromotionService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequiredArgsConstructor
@RestController
@RequestMapping
public class SavingController {
    private final SavingPromotionService savingPromotionService;

    @PostMapping("/relation")
    public ResponseEntity<String> createPromotionRelation(@RequestBody PromotionRequest request) {
        savingPromotionService.createPromotionRelation(request.getChannelId(), request.getPostId());
        return ResponseEntity.ok("홍보 관계 생성 실행 완료");
    }
}
