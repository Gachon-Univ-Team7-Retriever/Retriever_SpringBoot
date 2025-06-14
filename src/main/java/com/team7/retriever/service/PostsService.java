package com.team7.retriever.service;

import com.team7.retriever.dto.UpdateCheckRequest;
import com.team7.retriever.entity.Posts;
import com.team7.retriever.repository.PostsRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.data.domain.Sort;

import java.util.List;
import java.util.Optional;

@Service
public class PostsService {

    @Autowired
    private PostsRepository postsRepository;

    // 전체 게시글 조회
    public List<Posts> getAllPosts() {
        return postsRepository.findAll();
    }

    /* 241231 추가 */
    // Id로 조회
    public Optional<Posts> getPostById(String id) { return postsRepository.findById(id); }

    // 태그로 조회
    public List<Posts> getPostsByTag(String tag) {
        return postsRepository.findByTag(tag);
    }

    // 제목에 포함되는 것
    public List<Posts> getPostsByTitleContaining(String title) {
        return postsRepository.findByTitleContaining(title);
    }

    // 내용에 포함되는 것
    public List<Posts> getPostsByContentContaining(String content) {
        return postsRepository.findByContentContaining(content);
    }

    // 게시 사이트로 조회
    public List<Posts> getPostsBySiteName(String siteName) {
        return postsRepository.findBySiteName(siteName);
    }

    // 프로모션 링크로 조회
    /*
    public List<Posts> getPostsByPromoSiteLink(String promoSiteLink) {
        return postsRepository.findByPromoSiteLink(promoSiteLink);
    }
     */

    public List<Posts> getPostsByPromoSiteLink(String link) {
        return postsRepository.findByPromoSiteLinkContaining(link);
    }

    /*
    // 프로모션 이름으로 조회
    public List<Posts> getPostsByPromoSiteName(String promoSiteName) {
        return postsRepository.findByPromoSiteName(promoSiteName);
    }

     */

    // 홍보하는 채널 아이디로 조회
    public List<Posts> getPostsByPromoChannelId(String promoChannelId) {
        return postsRepository.findByPromoChannelId(promoChannelId);
    }

    // 게시글 작성자 이름으로 조회
    public List<Posts> getPostsByAuthor(String author) {
        return postsRepository.findByAuthor(author);
    }

    // 게시글 링크로 조회
    public List<Posts> getPostsByLink(String link) { return postsRepository.findByLink(link, Sort.by(Sort.Order.asc("createdAt"))); }

    /*
    // 전체 데이터 조회 + 삭제되지 않은 게시글만 필터링 + 링크만 반환
    public List<String> getAllPostsForUpdate() {
        return postsRepository.findAll().stream()
                .filter(post -> !post.isDeleted())
                .map(Posts::getLink)
                .toList();
    }

     */

    public List<UpdateCheckRequest> getAllPostsForUpdate() {
        return postsRepository.findAll().stream()
                .filter(post -> !post.isDeleted())
                .map(post -> new UpdateCheckRequest(
                        post.getLink(),
                        post.getTitle(),
                        post.getSource()
                ))
                .toList();
    }

    public void addChannelId(Posts post) {
        postsRepository.save(post);
    }
}
