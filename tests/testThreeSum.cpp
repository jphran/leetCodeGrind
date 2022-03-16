//
// Created by thera on 3/12/22.
//
#define CATCH_CONFIG_MAIN

#include "array/PostNimble/ThreeSum.h"
#include <catch2/catch.hpp>
#include <vector>

using namespace std;

TEST_CASE("Simple Fn Test 3Sum", "[3Sum]") {
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> ans = {{-1, -1, 2}, {-1, 0, 1}};

    Solution s;
    REQUIRE(s.threeSum(nums) == ans);
}

TEST_CASE("Simple Fn Test 3Sum1", "[3Sum]") {
    vector<int> nums = {};
    vector<vector<int>> ans = {};

    Solution s;
    REQUIRE(s.threeSum(nums) == ans);
}

TEST_CASE("Simple Fn Test 3Sum2", "[3Sum]") {
    vector<int> nums = {0};
    vector<vector<int>> ans = {};

    Solution s;
    REQUIRE(s.threeSum(nums) == ans);
}

TEST_CASE("Failed Test 3Sum", "[3Sum]") {
    vector<int> nums = {0, 0, 0};
    vector<vector<int>> ans = {{0, 0, 0}};

    Solution s;
    REQUIRE(s.threeSum(nums) == ans);
}

TEST_CASE("Failed Test 3Sum1", "[3Sum]") {
    vector<int> nums = {-2, 0, 1, 1, 2};
    vector<vector<int>> ans = {{-2, 0, 2}, {-2, 1, 1}};

    Solution s;
    REQUIRE(s.threeSum(nums) == ans);
}

TEST_CASE("Failed Test 3Sum2", "[3Sum]") {
    vector<int> nums = {3, 0, -2, -1, 1, 2};
    vector<vector<int>> ans = {{-2, -1, 3}, {-2, 0, 2}, {-1, 0, 1}};

    Solution s;
    REQUIRE(s.threeSum(nums) == ans);
}

TEST_CASE("Failed Test 3Sum3", "[3Sum]") {
    vector<int> nums = {-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4};
    vector<vector<int>> ans = {{-4, 0, 4}, {-4, 1, 3}, {-3, -1, 4}, {-3, 0, 3}, {-3, 1, 2}, {-2, -1, 3}, {-2, 0, 2}, {-1, -1, 2}, {-1, 0, 1}};

    Solution s;
    REQUIRE(s.threeSum(nums) == ans);
}

TEST_CASE("Failed Test 3Sum4", "[3Sum]") {
    vector<int> nums = {-2, 0, 0, 2, 2};
    vector<vector<int>> ans = {{-2, 0, 2}};

    Solution s;
    REQUIRE(s.threeSum(nums) == ans);
}