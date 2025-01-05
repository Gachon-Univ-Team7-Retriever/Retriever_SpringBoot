package com.team7.retriever.service;

import com.team7.retriever.entity.Posts;
import com.team7.retriever.repository.PostsRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PostsService {

    @Autowired
    private PostsRepository PostsRepository;

    // 전체 게시글 조회
    public List<Posts> getAllPosts() {
        return PostsRepository.findAll();
    }

    // 특정 게시글 ID로 조회
    public Posts getPostById(String id) {
        return PostsRepository.findById(id).orElse(null);
    }

    // 태그로 조회
    public List<Posts> getPostsByTag(String tag) {
        return PostsRepository.findByTag(tag);
    }

    // 제목에 포함되는 것
    public List<Posts> getPostsByTitleContaining(String title) {
        return PostsRepository.findByTitleContaining(title);
    }

    // 내용에 포함되는 것
    public List<Posts> getPostsByContentContaining(String content) {
        return PostsRepository.findByContentContaining(content);
    }

    // 게시 사이트로 조회
    public List<Posts> getPostsBySiteName(String siteName) {
        return PostsRepository.findBySiteName(siteName);
    }

    // 프로모션 링크로 조회
    public List<Posts> getPostsByPromoSiteLink(String promoSiteLink) {
        return PostsRepository.findByPromoSiteLink(promoSiteLink);
    }

    // 프로모션 이름으로 조회
    public List<Posts> getPostsByPromoSiteName(String promoSiteName) {
        return PostsRepository.findByPromoSiteName(promoSiteName);
    }

    // 게시글 작성자 이름으로 조회
    public List<Posts> getPostsByAuthor(String author) {
        return PostsRepository.findByAuthor(author);
    }
}
