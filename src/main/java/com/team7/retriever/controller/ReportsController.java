package com.team7.retriever.controller;

import com.team7.retriever.entity.Reports;
import com.team7.retriever.service.ReportsService;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Optional;

@RestController
@AllArgsConstructor
@RequestMapping("/report")
public class ReportsController {
    private final ReportsService reportsService;

    // 전체 조회
    @GetMapping("/all")
    public List<Reports> getAllReports() { return reportsService.getAllReports(); }

    // 아이디로 조회
    @GetMapping("/id")
    public Optional<Reports> getReportById(@RequestParam String id) { return reportsService.getReportById(id); }

    // 채널 아이디로 조회
    @GetMapping("/channelId")
    public List<Reports> getReportByChannelId(@RequestParam long channelId) { return reportsService.getReportByChId(channelId); }

    // type에 포함
    @GetMapping("/type")
    public List<Reports> getReportsByType(@RequestParam String type) { return reportsService.getReportsByType(type); }


    // content에 포함
    @GetMapping("/content")
    public List<Reports> getReportsByContent(@RequestParam String content) { return this.reportsService.getReportsByContent(content); }


    // description에 포함
    @GetMapping("/desc")
    public List<Reports> getReportsByDescription(@RequestParam String description) { return this.reportsService.getReportsByDescription(description); }

}
