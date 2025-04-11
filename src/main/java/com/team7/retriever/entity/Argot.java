package com.team7.retriever.entity;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import java.time.LocalDateTime;

@Getter
@Setter
@Document(collection = "argot")
public class Argot {

    /*
    @Id
    private String id;
    private String slang;
    private int count;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    */

    @Id
    private String _id;
    private String drugId;
    @Field("name")
    private String argot;
    private String description;

}
