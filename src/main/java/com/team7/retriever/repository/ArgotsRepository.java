package com.team7.retriever.repository;

import com.team7.retriever.entity.Argot;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ArgotsRepository extends MongoRepository<Argot, String> {

    // 전체 조회
    List<Argot> findAll();

    // 아이디로 조회
    Optional<Argot> findById(String id);

    // drugId로 조회
    List<Argot> findByDrugId(String drugId);

    // argot으로 조회 (은어) (포함) ; slang -> name 으로 변경
    @Query("{ 'argot':  { $regex:  ?0, $options: 'i' } }")
    List<Argot> findByArgot(String argot);

    // description으로 조회 (포함)
    @Query("{ 'description':  { $regex:  ?0, $options: 'i' } }")
    List<Argot> findByDescription(String desc);



    // count 많은 순으로 정렬 => count 삭제됨
    // List<Argot> findAllByOrderByCountDesc();
}
