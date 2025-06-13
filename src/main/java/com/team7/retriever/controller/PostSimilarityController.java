package com.team7.retriever.controller;


import com.team7.retriever.entity.PostSimilarity;
import com.team7.retriever.service.PostSimilarityService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("/post-similarity")
public class PostSimilarityController {

    private final PostSimilarityService postSimilarityService;

    // 전체 조회
    @GetMapping("/all")
    public List<PostSimilarity> getAllPostSimilarities() {
        return postSimilarityService.getAllPostSimilarities();
    }

    /* 250117 수정 */
    // 아이디로 조회
    @GetMapping("/id/{id}")
    public PostSimilarity getPostSimilarityById(@PathVariable String id) {
        return postSimilarityService.getPostSimilarityById(id);
    }

    // 포스트 아이디로 조회 (기준 게시글)
    @GetMapping("/post/{postId}")
    public PostSimilarity getPostSimilarityByPostId(@PathVariable String postId) {
        return postSimilarityService.getPostSimilarityByPostId(postId);
    }
}