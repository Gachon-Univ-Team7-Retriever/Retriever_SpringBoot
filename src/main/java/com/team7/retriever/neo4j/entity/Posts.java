package com.team7.retriever.neo4j.entity;

import lombok.*;
import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;
import org.springframework.data.neo4j.core.schema.Relationship;

import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Set;

@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Node("Posts")
public class Posts {

    @Id
    private String postId;
    private Long channelId;
    private String content;
    private String link;
    private String siteName;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    @Builder.Default
    @Relationship(type = "PROMOTES", direction = Relationship.Direction.OUTGOING)
    private Set<Promotes> promotedByChannels = new HashSet<>();

}
