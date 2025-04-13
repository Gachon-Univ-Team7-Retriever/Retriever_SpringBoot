package com.team7.retriever.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;
import java.util.List;

@Getter
@NoArgsConstructor
@AllArgsConstructor
public class ChatArgotDrugDTO {

    private int id;
    private List<String> argot;
    private List<String> drugs;
    private LocalDateTime timestamp;
}
