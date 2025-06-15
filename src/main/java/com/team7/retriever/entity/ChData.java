package com.team7.retriever.entity;

import lombok.Getter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;

import java.time.LocalDateTime;
import java.util.List;

@Getter
@Document(collection = "channel_data")
public class ChData {

    // _id 자동 생성
    @Id
    @Field("_id")
    private String _id;
    private long channelId;
    private LocalDateTime timestamp;
    private String text;
    private SenderInfo sender;
    private Integer views; // *** null 일 수도 있는 값은 primitive -> Wrapper ***
    private String url;
    @Field("id")
    private int id;
    private Media media;
    private List<String> argot;
    private List<String> drugs;

    @Getter
    public static class SenderInfo {
        private String type;
        private String name;
        @Field("senderId")
        private long senderId;
    }

    @Getter
    public static class Media {
        private String url;
        private String type;
    }

}
