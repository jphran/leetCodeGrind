//
// Created by thera on 2/4/22.
//

#define CATCH_CONFIG_MAIN

#include "array/PostNimble/MaximumSubarray.h"
#include <catch2/catch.hpp>
#include <vector>

TEST_CASE("Simple Fn Test", "[MaximumSubarray]") {
    std::vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
    int ans = 6;

    Solution s;
    REQUIRE(s.maxSubArray(nums) == ans);
}