package com.team7.retriever.neo4j.service;

import com.team7.retriever.neo4j.repository.NeoChannelRepository;
import com.team7.retriever.neo4j.repository.NeoPostsRepository;
import com.team7.retriever.neo4j.entity.Channel;
import com.team7.retriever.neo4j.entity.Posts;
import com.team7.retriever.neo4j.entity.Promotes;
import com.team7.retriever.service.PostsService;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
@Slf4j
@RequiredArgsConstructor
public class SavingPromotionService {

    private final NeoChannelRepository neoChannelRepository;
    private final NeoPostsRepository neoPostsRepository;
    private final PostsService postsService;

    @Transactional
    public void createPromotionRelation(Long channelId, String postId) {
        // 채널 노드 조회 or 생성
        Channel channel = neoChannelRepository.findByChannelId(channelId)
                .orElseGet(() -> {
                    Channel newChannel = new Channel();
                    newChannel.setChannelId(channelId);
                    return neoChannelRepository.save(newChannel);
                });

        Optional<com.team7.retriever.entity.Posts> mongoPostOpt = postsService.getPostById(postId);
        if (mongoPostOpt.isEmpty()) {
            log.error("[Neo4j Service] MongoDB에서 해당 Post(" + postId + ")를 찾을 수 없습니다.");
        }
        com.team7.retriever.entity.Posts mongoPost = mongoPostOpt.get();

        // 포스트 노드 조회 or 생성
        Posts post = neoPostsRepository.findByPostId(postId)
                .orElseGet(() -> {
                    Posts newPost = Posts.builder()
                            .postId(postId)
                            .channelId(channelId)
                            .content(mongoPost.getContent())
                            .link(mongoPost.getLink())
                            .siteName(mongoPost.getSource() != null ? mongoPost.getSource() : mongoPost.getSiteName())
                            .createdAt(mongoPost.getCreatedAt())
                            .updatedAt(mongoPost.getUpdatedAt())
                            .build();
                    log.info("[Neo4j Service] Neo4j에 Post 데이터 생성: postId = " + postId);
                    return neoPostsRepository.save(newPost);
                });

        // 관계 중복 방지 - 관계가 없으면 추가
        boolean alreadyPromoted = channel.getPromotedPosts().stream()
                .anyMatch(promotes -> promotes.getPost().getPostId().equals(postId));

        if (!alreadyPromoted) {
            Promotes promotes = new Promotes(post);
            channel.getPromotedPosts().add(promotes);
            neoChannelRepository.save(channel);  // 관계도 같이 저장됨
            System.out.println("[Neo4j Service] 홍보 관계 생성 완료");
            log.info("[Neo4j Service] 홍보 관계 생성 완료");
        } else {
            System.out.println("[Neo4j Service] 이미 관계가 존재합니다");
            log.info("[Neo4j Service] 이미 관계가 존재합니다");
        }
    }

}
