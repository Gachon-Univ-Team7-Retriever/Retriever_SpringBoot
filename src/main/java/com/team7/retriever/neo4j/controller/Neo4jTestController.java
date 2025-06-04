package com.team7.retriever.neo4j.controller;

import org.springframework.data.neo4j.core.Neo4jClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Neo4jTestController {

    private final Neo4jClient neo4jClient;

    public Neo4jTestController(Neo4jClient neo4jClient) {
        this.neo4jClient = neo4jClient;
    }

    @GetMapping("/neo4j-test")
    public String testConnection() {
        String greeting = neo4jClient.query("RETURN 'Hello Neo4j!' AS message")
                .fetchAs(String.class)
                .one()
                .orElse("No response");
        return greeting;
    }

}
