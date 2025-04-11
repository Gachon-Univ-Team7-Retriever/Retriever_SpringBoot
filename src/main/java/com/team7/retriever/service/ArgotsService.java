package com.team7.retriever.service;


import com.team7.retriever.entity.Argot;
import com.team7.retriever.repository.ArgotsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class ArgotsService {

    @Autowired
    private ArgotsRepository argotsRepository;

    // 전체 조회
    public List<Argot> getAllArgots() {
        return argotsRepository.findAll();
    }

    // 아이디로 조회
    public Optional<Argot> getArgotById(String id) {
        return argotsRepository.findById(id);
    }

    // drugId로 조회
    public List<Argot> getArgotByDrugId(String drugId) { return argotsRepository.findByDrugId(drugId); }

    // argot으로 조회 ; slang -> argot (name) 으로 변경
    public List<Argot> getArgotsByArgot(String argot) {
        return argotsRepository.findByArgot(argot);
    }

    // description으로 조회
    public List<Argot> getArgotByDescription(String desc) { return argotsRepository.findByDescription(desc); }



    /*
    // count 많은 순으로 조회
    public List<Argot> getSlangsSortedByCount() {
        return slangsRepository.findAllByOrderByCountDesc();
    }

     */

    // DB에서 slang 리스트로 받아오기
    public List<String> getAllArgotsToList() {
        return argotsRepository.findAll() // DB에서 전체 조회
                .stream()
                .map(Argot::getArgot) // argot 필드만 추출
                .filter(argot -> argot != null) // argot이 null이 아닌 경우만
                .map(argot -> "t.me " + argot) // 각 argot 앞에 t.me 추가
                .collect(Collectors.toList()); // 리스트로 변환
    }
}