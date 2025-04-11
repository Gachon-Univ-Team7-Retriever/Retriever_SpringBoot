package com.team7.retriever.entity;

import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import java.time.LocalDateTime;
import java.util.List;

@Getter
@Setter
@Document(collection = "drugs")
public class Drugs {

    @Id
    private String _id;
    private String drugName;
    private String drugType;
    private String drugEnName;

}
