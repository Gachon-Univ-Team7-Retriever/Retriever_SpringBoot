package com.team7.retriever.repository;


import com.team7.retriever.entity.Drugs;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import java.util.List;
import java.util.Optional;

public interface DrugsRepository extends MongoRepository<Drugs, String> {

    // 전체 조회
    List<Drugs> findAll();

    // 아이디로 조회
    Optional<Drugs> findById(String id);

    // 이름으로 조회
    @Query("{ 'drugName':  { $regex:  ?0, $options: 'i' } }")
    List<Drugs> findByDrugName(String drugName);

    // 타입으로 조회
    @Query("{ 'drugType':  { $regex:  ?0, $options: 'i' } }")
    List<Drugs> findByDrugType(String drugType);

    /*
    // 상태로 조회
    List<Drugs> findByStatus(String status);

     */

    /*
    // count 큰 순으로 정렬하여 전체 조회
    List<Drugs> findAllByOrderByCountDesc();

    // count 큰 순으로 정렬하고 특정 타입만 조회
    List<Drugs> findByDrugTypeOrderByCountDesc(String drugType);

    // count 큰 순으로 정렬하고 특정 상태만 조회
    List<Drugs> findByStatusOrderByCountDesc(String status);

     */
}

