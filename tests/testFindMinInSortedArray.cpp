//
// Created by thera on 3/8/22.
//

#define CATCH_CONFIG_MAIN

#include "array/PostSarcos/findMinInRotatedSortedArray.h"
#include <catch2/catch.hpp>

TEST_CASE("Simple Fn Test findMin", "[FindMinInRotatedSortedArray]") {
    std::vector<int> input = {3,4,5,1,2};
    int ans = 1;

    Solution s;
    REQUIRE(s.findMin(input) == ans);
}

TEST_CASE("Simple Fn Test1 findMin", "[FindMinInRotatedSortedArray]") {
    std::vector<int> input = {4,5,6,7,0,1,2};
    int ans = 0;

    Solution s;
    REQUIRE(s.findMin(input) == ans);
}

TEST_CASE("Simple Fn Test2 findMin", "[FindMinInRotatedSortedArray]") {
    std::vector<int> input = {11,13,15,17};
    int ans = 11;

    Solution s;
    REQUIRE(s.findMin(input) == ans);
}

TEST_CASE("Failed Test findMin", "[FindMinInRotatedSortedArray]") {
    std::vector<int> input = {2,1};
    int ans = 1;

    Solution s;
    REQUIRE(s.findMin(input) == ans);
}

TEST_CASE("Failed Test1 findMin", "[FindMinInRotatedSortedArray]") {
    std::vector<int> input = {2,3,4,5,1};
    int ans = 1;

    Solution s;
    REQUIRE(s.findMin(input) == ans);
}

TEST_CASE("Failed Test12findMin", "[FindMinInRotatedSortedArray]") {
    std::vector<int> input = {9,1,2,3,4,5,6,7,8};
    int ans = 1;

    Solution s;
    REQUIRE(s.findMin(input) == ans);
}