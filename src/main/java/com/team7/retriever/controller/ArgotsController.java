package com.team7.retriever.controller;


import com.team7.retriever.entity.Argot;
import com.team7.retriever.service.ArgotsService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@AllArgsConstructor
@RequestMapping("/argots") // MODI
public class ArgotsController {

    private final ArgotsService argotsService;

    // 전체 조회
    @GetMapping("/all")
    public List<Argot> getAllArgots() {
        return argotsService.getAllArgots();
    }

    // 아이디로 조회
    @GetMapping("/id/{id}") /* 250106 수정 */
    public Optional<Argot> getArgotById(@PathVariable String id) {
        return argotsService.getArgotById(id);
    }

    // drugId로 조회
    @GetMapping("/drug/{drugId}")
    public List<Argot> getArgotByDrugId(@PathVariable String drugId) { return argotsService.getArgotByDrugId(drugId); }

    // argot으로 조회
    @GetMapping("/argot/{argot}") // MODI
    public List<Argot> getArgotsByArgot(@PathVariable String argot) {
        return argotsService.getArgotsByArgot(argot);
    }

    // desctiption으로 조회
    @GetMapping("/desc")
    public List<Argot> getArgotsByDescription(@RequestParam String desc) { return argotsService.getArgotByDescription(desc); }

    /*
    // count 많은 순으로 정렬하여 전체 조회
    @GetMapping("/sorted")
    public List<Argot> getSlangsSortedByCount() {
        return argotsService.getSlangsSortedByCount();
    }

     */
}
