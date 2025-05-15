package com.team7.retriever.service;

import com.team7.retriever.entity.Reports;
import com.team7.retriever.repository.ReportsRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ReportsService {
    private final ReportsRepository reportsRepository;
    public ReportsService(ReportsRepository reportsRepository) {
        this.reportsRepository = reportsRepository;
    }

    // 전체 조회
    public List<Reports> getAllReports() {
        return reportsRepository.findAll();
    }

    // 아이디로 조회
    public Optional<Reports> getReportById(String id) {
        return reportsRepository.findById(id);
    }

    // 채널 아이디로 조회
    public List<Reports> getReportByChId(long chId) {
        return reportsRepository.findByChannelId(chId);
    }

    // type에 포함
    public List<Reports> getReportsByType(String type) {
        return reportsRepository.findByType(type);
    }

    // content에 포함
    public List<Reports> getReportsByContent(String content) {
        return reportsRepository.findByContent(content);
    }

    // description에 포함
    public List<Reports> getReportsByDescription(String description) {
        return reportsRepository.findByDescription(description);
    }
}
