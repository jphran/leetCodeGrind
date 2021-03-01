//
// Created by jfrancis on 2/28/21.
//

#include <iostream>
#include <catch2/catch_all.hpp>
#include <catch2/catch_test_macros.hpp>
#include <TwoSum.h>

TEST_CASE("Given an array of integers nums "
          "and an integer target, return indices of "
          "the two numbers such that they add up to target", "[TwoSum]") {

    std::vector<int> nums{2,7,11,15};
    int target = 9;
    Solution s;
    auto vals = s.twoSum(nums, target);
    for(int val : vals)
      std::cout << val << std::endl;
    REQUIRE(vals.at(0) == 0);
}