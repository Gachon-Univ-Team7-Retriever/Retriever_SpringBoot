package com.team7.retriever.entity;

import lombok.Getter;
import org.bson.types.ObjectId;
import org.springframework.cglib.core.Local;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.LocalDateTime;
import java.util.List;

@Getter
@Document(collection = "channel_data")
public class ChData {

    // _id 자동 생성
    @Id
    private String id;
    private int channelId;
    private LocalDateTime timestamp;
    private String text;
    private senderInfo sender;
    private int views;
    private String url;
    private int index;
    private media media;

    @Getter
    public static class senderInfo {
        private String type;
        private String name;
        private String senderId;
    }

    @Getter
    public static class media {
        private String url;
        private String type;
    }
}
