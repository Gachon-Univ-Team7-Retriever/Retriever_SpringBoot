package com.team7.retriever.controller;

import com.team7.retriever.dto.BookmarksRequest;
import com.team7.retriever.entity.Bookmarks;
import com.team7.retriever.service.BookmarksService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/bookmarks")
public class BookmarksController {

    private final BookmarksService BookmarksService;

    @Autowired
    public BookmarksController(BookmarksService BookmarksService) {
        this.BookmarksService = BookmarksService;
    }

    // 모든 북마크 조회
    @GetMapping("/all") /* 241231 수정 */
    public ResponseEntity<List<Bookmarks>> getAllBookmarks() {
        List<Bookmarks> bookmarks = BookmarksService.getAllBookmarks();
        return ResponseEntity.ok(bookmarks);
    }

    // 특정 유저 ID로 북마크 조회
    @GetMapping("/user/{userId}")
    public ResponseEntity<List<Bookmarks>> getBookmarksByUserId(@PathVariable String userId) {
        List<Bookmarks> bookmarks = BookmarksService.getBookmarksByUserId(userId);
        return ResponseEntity.ok(bookmarks);
    }

    // 특정 북마크 ID로 북마크 조회
    @GetMapping("/id/{id}") /* 241231 수정 */
    public ResponseEntity<Bookmarks> getBookmarkById(@PathVariable String id) {
        Optional<Bookmarks> bookmark = BookmarksService.getBookmarksById(id);
        return bookmark.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    // 새로운 북마크 추가
    @PostMapping("/add")
    public String addBookmark(@RequestBody BookmarksRequest request) {
        Bookmarks bookmark = new Bookmarks();
        bookmark.setChannelId(request.getChannelId());
        bookmark.setUserId(request.getUserId());

        // 나머지 값들 자동 설정
        bookmark.setDefaultValues();

        // 저장
        BookmarksService.saveBookmark(bookmark);

        // test code
        return "Bookmark created successfully";
    }


    // 특정 ID의 북마크 삭제 (북마크 아이디)
    @DeleteMapping("/delete/{id}")
    public ResponseEntity<Void> deleteBookmark(@PathVariable String id) {
        BookmarksService.deleteBookmarkById(id);
        return ResponseEntity.noContent().build();
    }
}
