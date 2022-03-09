//
// Created by jfrancis on 3/2/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include "array/TwoSum2.h"

//********************TWO SUM*************************
TEST_CASE("Given an array of integers nums and an integer target, "
          "return indices of the two numbers such that they add up to target."
, "[TwoSum]") {

    std::vector<int> nums{2,7,11,15};
    int target = 9;
    std::vector<int> ans{0,1};
    Solution s;

    REQUIRE(s.twoSum(nums, target) == ans);
}

TEST_CASE("Test 2", "[TwoSum]") {
    std::vector<int> nums{3,2,4};
    int target = 6;
    std::vector<int> ans{1,2};
    Solution s;

    REQUIRE(s.twoSum(nums, target) == ans);
}

