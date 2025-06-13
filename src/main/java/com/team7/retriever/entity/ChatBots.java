package com.team7.retriever.entity;

import lombok.Getter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Getter
@Document(collection = "chat_bot")
public class ChatBots {
    @Id
    private long id;
    private List<Long> channels;
    private LocalDateTime updatedAt;
    private List<String> chats;
    private String scope;
}
