package com.team7.retriever.neo4j.entity;

import lombok.Getter;
import org.springframework.data.neo4j.core.schema.GeneratedValue;
import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.RelationshipProperties;
import org.springframework.data.neo4j.core.schema.TargetNode;

@Getter
@RelationshipProperties
public class Promotes {

    @Id
    @GeneratedValue
    private Long id;

    @TargetNode
    private Posts post;

    public Promotes(Posts post) {
        this.post = post;
    }

}

