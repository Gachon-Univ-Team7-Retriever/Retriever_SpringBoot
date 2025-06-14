package com.team7.retriever;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.neo4j.core.mapping.Neo4jMappingContext;
import org.springframework.scheduling.annotation.EnableScheduling;

@EnableScheduling // Scheduler 활성화
@SpringBootApplication
public class RetrieverApplication {

    public static void main(String[] args) {
        SpringApplication.run(RetrieverApplication.class, args);
    }

}
