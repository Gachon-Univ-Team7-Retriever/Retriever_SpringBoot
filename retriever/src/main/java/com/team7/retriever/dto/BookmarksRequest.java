package com.team7.retriever.dto;


public class BookmarksRequest {
    private String channelId;
    private String userId;

    // 기본 생성자
    public BookmarksRequest() {
    }

    // 생성자
    public BookmarksRequest(String channelId, String userId) {
        this.channelId = channelId;
        this.userId = userId;
    }

    // getter & setter
    public String getChannelId() {
        return channelId;
    }

    public void setChannelId(String channelId) {
        this.channelId = channelId;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }
}
