package com.team7.retriever.entity;

import lombok.Getter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;

@Getter
@Document(collection = "reports")
public class Reports {

    @Id
    private String id;
    private long channelId;
    private int chatId;
    private String type;
    private String content;
    private String description;
    private LocalDateTime timestamp;
}
