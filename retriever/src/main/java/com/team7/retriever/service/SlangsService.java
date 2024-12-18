package com.team7.retriever.service;


import com.team7.retriever.entity.Slangs;
import com.team7.retriever.repository.SlangsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class SlangsService {

    @Autowired
    private SlangsRepository slangsRepository;

    // 아이디로 조회
    public Optional<Slangs> getSlangById(String id) {
        return slangsRepository.findById(id);
    }

    // slang으로 조회
    public List<Slangs> getSlangBySlang(String slang) {
        return slangsRepository.findBySlang(slang);
    }

    // 전체 조회
    public List<Slangs> getAllSlangs() {
        return slangsRepository.findAll();
    }

    // count 많은 순으로 조회
    public List<Slangs> getSlangsSortedByCount() {
        return slangsRepository.findAllByOrderByCountDesc();
    }
}