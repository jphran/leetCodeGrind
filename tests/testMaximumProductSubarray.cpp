//
// Created by thera on 2/23/22.
//

#define CATCH_CONFIG_MAIN

#include "array/PostNimble/MaximumProductSubarray.h"
#include <catch2/catch.hpp>
#include <vector>

TEST_CASE("Simple Fn Test", "[MaximumProductSubarray]") {
    std::vector<int> nums = {2,3,-2,4};
    int ans = 6;

    Solution s;
    REQUIRE(s.maxProduct(nums) == ans);
}

TEST_CASE("Simple Fn Test1", "[MaximumProductSubarray]") {
    std::vector<int> nums = {-2,0,-1};
    int ans = 0;

    Solution s;
    REQUIRE(s.maxProduct(nums) == ans);
}

TEST_CASE("Failed Test", "[MaximumProductSubarray]") {
    std::vector<int> nums = {-2, 3, -4};
    int ans = 24;

    Solution s;
    REQUIRE(s.maxProduct(nums) == ans);
}

TEST_CASE("Failed Test1", "[MaximumProductSubarray]") {
    std::vector<int> nums = {-2};
    int ans = -2;

    Solution s;
    REQUIRE(s.maxProduct(nums) == ans);
}

TEST_CASE("Failed Test2", "[MaximumProductSubarray]") {
    std::vector<int> nums = {2,-5,-2,-4,3};
    int ans = 24;

    Solution s;
    REQUIRE(s.maxProduct(nums) == ans);
}