package com.team7.retriever.controller;

import com.team7.retriever.entity.Posts;
import com.team7.retriever.service.PostsService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@AllArgsConstructor
@RequestMapping("/posts")
public class PostsController {

    private final PostsService postsService;

    // 전체 게시글 조회
    @GetMapping("/all")
    public List<Posts> getAllPosts() {
        return postsService.getAllPosts();
    }
    
    /* 241231 추가 */
    // Id로 조회
    @GetMapping("/id/{id}") 
    public Optional<Posts> getPostById(@PathVariable String id) { return postsService.getPostById(id); }

    // null
    // 태그로 조회
    @GetMapping("/tag/{tag}")
    public List<Posts> getPostsByTag(@PathVariable String tag) {
        return postsService.getPostsByTag(tag);
    }

    // 제목에 포함되는 것
    @GetMapping("/title/{title}")
    public List<Posts> getPostsByTitleContaining(@PathVariable String title) {
        return postsService.getPostsByTitleContaining(title);
    }

    // 내용에 포함되는 것
    @GetMapping("/content/{content}")
    public List<Posts> getPostsByContentContaining(@PathVariable String content) {
        return postsService.getPostsByContentContaining(content);
    }

    // 게시 사이트로 조회
    @GetMapping("/site/{siteName}")
    public List<Posts> getPostsBySiteName(@PathVariable String siteName) {
        return postsService.getPostsBySiteName(siteName);
    }

    // promo == 타고 넘어가는 판매 사이트(채널)
    // 프로모션 링크로 조회
    @GetMapping("/promoLink")
    public List<Posts> getPostsByPromoSiteLink(@RequestParam String promoSiteLink) {
        return postsService.getPostsByPromoSiteLink(promoSiteLink);
    }

    /*
    // 프로모션 이름으로 조회
    @GetMapping("/promoName/{promoSiteName}")
    public List<Posts> getPostsByPromoSiteName(@PathVariable String promoSiteName) {
        return postsService.getPostsByPromoSiteName(promoSiteName);
    }

     */

    // 홍보하는 채널 아이디로 조회
    @GetMapping("/promoChannelId/{promoChannelId}")
    public List<Posts> getPostsByPromoChannelId(@PathVariable String promoChannelId) {
        return postsService.getPostsByPromoChannelId(promoChannelId);
    }

    // 게시글 작성자 이름으로 조회
    @GetMapping("/author/{author}")
    public List<Posts> getPostsByAuthor(@PathVariable String author) {
        return postsService.getPostsByAuthor(author);
    }

    // 해당 링크로 조회 -> 모든 버전 조회 (수집 시점 순)
    @GetMapping("/url")
    public List<Posts> getPostsByLink(@RequestParam String url) {
        return postsService.getPostsByLink(url);
    }
}
