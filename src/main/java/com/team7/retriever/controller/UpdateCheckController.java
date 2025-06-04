package com.team7.retriever.controller;

import com.team7.retriever.dto.PostUpdateRequest;
import com.team7.retriever.dto.UpdateCheckRequest;
import com.team7.retriever.service.PostsService;
import com.team7.retriever.service.PreprocessService;
import com.team7.retriever.service.UpdateCheckService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/post-update")
public class UpdateCheckController {
    @Autowired
    PostsService postsService;
    @Autowired
    private PreprocessService preprocessService;
    @Autowired
    private UpdateCheckService updateCheckService;

    // DB 데이터 조회 결과 테스트
    @GetMapping("/posts")
    public List<UpdateCheckRequest> getPosts() {
        return postsService.getAllPostsForUpdate();
    }

    @GetMapping
    public void updateAllPostsTest() {
        updateCheckService.updateAllPost();
    }

    // Post 업데이트 테스트
    @PostMapping("/test")
    public String updateTest(@RequestBody PostUpdateRequest postUpdateRequest) {
        String html = postUpdateRequest.getHtml();
        String link = postUpdateRequest.getLink();
        String title = postUpdateRequest.getTitle();
        String source = postUpdateRequest.getSource();

        return preprocessService.updatePreprocess(html, link, title, source);
    }
}
