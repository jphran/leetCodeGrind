//
// Created by jfrancis on 7/20/21.
//

#define CATCH_CONFIG_MAIN

#include "array/PostSarcos/ContainsDuplicate.h"
#include <catch2/catch.hpp>

//********************CONTAINS DUPLICATE*************************
TEST_CASE("Given an integer array nums, return true if any value appears at least twice in the array, "
          "and return false if every element is distinct."
, "[ContainsDuplicate]") {

    std::vector<int> nums{2,7,11,15};
    Solution s;

    REQUIRE(s.containsDuplicate(nums) == false);
}

TEST_CASE("Basic fn 1", "[ContainsDuplicate]") {

    std::vector<int> nums{2,7,11,2};
    Solution s;

    REQUIRE(s.containsDuplicate(nums) == true);
}

TEST_CASE("Basic fn 2", "[ContainsDuplicate]") {

    std::vector<int> nums{};
    for(int i = 0; i < 100; ++i)
        nums.push_back(i);
    nums.at(1) = 0;

    Solution s;

    REQUIRE(s.containsDuplicate(nums) == true);
}