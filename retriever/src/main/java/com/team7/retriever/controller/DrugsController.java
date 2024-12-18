package com.team7.retriever.controller;


import com.team7.retriever.entity.Drugs;
import com.team7.retriever.service.DrugsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/drugs")
public class DrugsController {

    @Autowired
    private DrugsService drugsService;

    // 아이디로 조회
    @GetMapping("/{id}")
    public Optional<Drugs> getDrugById(@PathVariable String id) {
        return drugsService.getDrugById(id);
    }
    // 굳이 필요는 없을 것

    // 이름으로 조회
    @GetMapping("/name/{drugName}")
    public List<Drugs> getDrugsByName(@PathVariable String drugName) {
        return drugsService.getDrugsByName(drugName);
    }

    // 타입으로 조회
    @GetMapping("/type/{drugType}")
    public List<Drugs> getDrugsByType(@PathVariable String drugType) {
        return drugsService.getDrugsByType(drugType);
    }

    // 상태로 조회
    @GetMapping("/status/{status}")
    public List<Drugs> getDrugsByStatus(@PathVariable String status) {
        return drugsService.getDrugsByStatus(status);
    }

    // 전체 조회
    @GetMapping("/all")
    public List<Drugs> getAllDrugs() {
        return drugsService.getAllDrugs();
    }

    // count 큰 순으로 정렬하여 [전체] 조회
    @GetMapping("/sorted")
    public List<Drugs> getDrugsSortedByCount() {
        return drugsService.getDrugsSortedByCount();
    }

    // count 큰 순으로 정렬하고 [특정 타입]만 조회
    @GetMapping("/sorted/type/{drugType}")
    public List<Drugs> getDrugsByTypeSortedByCount(@PathVariable String drugType) {
        return drugsService.getDrugsByTypeSortedByCount(drugType);
    }

    // count 큰 순으로 정렬하고 [특정 상태]만 조회
    @GetMapping("/sorted/status/{status}")
    public List<Drugs> getDrugsByStatusSortedByCount(@PathVariable String status) {
        return drugsService.getDrugsByStatusSortedByCount(status);
    }
}
