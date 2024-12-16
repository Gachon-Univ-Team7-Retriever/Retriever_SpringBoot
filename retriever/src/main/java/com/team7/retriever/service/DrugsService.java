package com.team7.retriever.service;


import com.team7.retriever.entity.Drugs;
import com.team7.retriever.repository.DrugsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DrugsService {

    @Autowired
    private DrugsRepository drugsRepository;

    // 아이디로 조회
    public Optional<Drugs> getDrugById(String id) {
        return drugsRepository.findById(id);
    }

    // 이름으로 조회
    public List<Drugs> getDrugsByName(String drugName) {
        return drugsRepository.findByDrugName(drugName);
    }

    // 타입으로 조회
    public List<Drugs> getDrugsByType(String drugType) {
        return drugsRepository.findByDrugType(drugType);
    }

    // 상태로 조회
    public List<Drugs> getDrugsByStatus(String status) {
        return drugsRepository.findByStatus(status);
    }

    // 전체 조회
    public List<Drugs> getAllDrugs() {
        return drugsRepository.findAll();
    }

    // count 큰 순으로 정렬해서 전체 조회
    public List<Drugs> getDrugsSortedByCount() {
        return drugsRepository.findAllByOrderByCountDesc();
    }

    // count 큰 순으로 정렬하고 특정 타입만 조회
    public List<Drugs> getDrugsByTypeSortedByCount(String drugType) {
        return drugsRepository.findByDrugTypeOrderByCountDesc(drugType);
    }

    // count 큰 순으로 정렬하고 특정 상태만 조회
    public List<Drugs> getDrugsByStatusSortedByCount(String status) {
        return drugsRepository.findByStatusOrderByCountDesc(status);
    }
}
