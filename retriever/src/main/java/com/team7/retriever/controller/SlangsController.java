package com.team7.retriever.controller;


import com.team7.retriever.entity.Slangs;
import com.team7.retriever.service.SlangsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/slangs")
public class SlangsController {

    @Autowired
    private SlangsService slangsService;

    // 전체 조회
    @GetMapping("/all")
    public List<Slangs> getAllSlangs() {
        return slangsService.getAllSlangs();
    }

    // 아이디로 조회
    @GetMapping("/{id}")
    public Optional<Slangs> getSlangById(@PathVariable String id) {
        return slangsService.getSlangById(id);
    }

    // slang으로 조회
    @GetMapping("/slang/{slang}")
    public List<Slangs> getSlangBySlang(@PathVariable String slang) {
        return slangsService.getSlangBySlang(slang);
    }

    // count 많은 순으로 정렬하여 전체 조회
    @GetMapping("/sorted")
    public List<Slangs> getSlangsSortedByCount() {
        return slangsService.getSlangsSortedByCount();
    }
}
