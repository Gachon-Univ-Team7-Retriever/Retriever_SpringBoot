package com.team7.retriever.neo4j.entity;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;
import org.springframework.data.neo4j.core.schema.Relationship;

import java.util.HashSet;
import java.util.Set;

@Getter
@Setter
@Node("Channel")
public class Channel {

    @Id
    private Long channelId;

    @Relationship(type = "PROMOTES", direction = Relationship.Direction.INCOMING)
    private Set<Promotes> promotedPosts = new HashSet<>();

}
