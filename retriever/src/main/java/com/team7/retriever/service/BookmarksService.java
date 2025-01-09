package com.team7.retriever.service;

import com.team7.retriever.entity.Bookmarks;
import com.team7.retriever.repository.BookmarksRepository;
import com.team7.retriever.repository.ChDataRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class BookmarksService {
    @Autowired
    private BookmarksRepository BookmarksRepository;

    @Autowired
    public BookmarksService(ChDataRepository chDataRepository) {
        this.BookmarksRepository = BookmarksRepository;
    }

    // 전체 조회
    public List<Bookmarks> getAllBookmarks() {
        return BookmarksRepository.findAll();
    }

    // 유저 아이디로 조회
    public List<Bookmarks> getBookmarksByUserId(String userId) {
        return BookmarksRepository.findByUserId(userId);
    }

    // 아이디로 조회
    public Optional<Bookmarks> getBookmarksById(String id) {
        return BookmarksRepository.findById(id);
    }

    // 북마크 추가
    public void saveBookmark(Bookmarks newBookmark) {
        BookmarksRepository.save(newBookmark);
    }

    // 아이디로 삭제
    public void deleteBookmarkById(String id) {
        BookmarksRepository.deleteById(id);
    }

}