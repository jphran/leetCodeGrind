//
// Created by thera on 3/12/22.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include <vector>
#include "array/SearchInRotatedSortedArray.h"

TEST_CASE("Simple Fn Test Search", "[SearchInRotatedSortedArray]") {
    std::vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    int target = 0;
    int ans = 4;

    Solution s;
    REQUIRE(s.search(nums, target) == ans);
}

TEST_CASE("Simple Fn Test Search1", "[SearchInRotatedSortedArray]") {
    std::vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    int target = 3;
    int ans = -1;

    Solution s;
    REQUIRE(s.search(nums, target) == ans);
}

TEST_CASE("Simple Fn Test Search2", "[SearchInRotatedSortedArray]") {
    std::vector<int> nums = {1};
    int target = 0;
    int ans = -1;

    Solution s;
    REQUIRE(s.search(nums, target) == ans);
}

TEST_CASE("Failed Test Search", "[SearchInRotatedSortedArray]") {
    std::vector<int> nums = {5, 1, 2, 3, 4};
    int target = 1;
    int ans = 1;

    Solution s;
    REQUIRE(s.search(nums, target) == ans);
}

TEST_CASE("Failed Test Search1", "[SearchInRotatedSortedArray]") {
    std::vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    int target = 5;
    int ans = 1;

    Solution s;
    REQUIRE(s.search(nums, target) == ans);
}

TEST_CASE("Failed Test Search2", "[SearchInRotatedSortedArray]") {
    std::vector<int> nums = {8, 9, 2, 3, 4};
    int target = 9;
    int ans = 1;

    Solution s;
    REQUIRE(s.search(nums, target) == ans);
}
