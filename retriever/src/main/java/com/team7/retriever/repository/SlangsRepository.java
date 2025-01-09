package com.team7.retriever.repository;

import com.team7.retriever.entity.Slangs;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface SlangsRepository extends MongoRepository<Slangs, String> {
    // 아이디로 조회
    Optional<Slangs> findById(String id);

    // slang으로 조회 (은어)
    List<Slangs> findBySlang(String slang);

    // 전체 조회
    List<Slangs> findAll();

    // count 많은 순으로 정렬
    List<Slangs> findAllByOrderByCountDesc();
}
