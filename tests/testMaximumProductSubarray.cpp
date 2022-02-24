//
// Created by thera on 2/23/22.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include <vector>
#include "array/MaximumProductSubarray.h"

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