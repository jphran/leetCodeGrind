//
// Created by thera on 3/12/22.
//

#define CATCH_CONFIG_MAIN

#include "array/PostNimble/MaxArea.h"
#include <catch2/catch.hpp>
#include <vector>

using namespace std;

TEST_CASE("Simple Fn Test ContainerWithMostWater", "[ContainerWithMostWater]") {
    vector<int> nums = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int ans = 49;

    Solution s;
    REQUIRE(s.maxArea(nums) == ans);
}

TEST_CASE("Simple Fn Test ContainerWithMostWater1", "[ContainerWithMostWater]") {
    vector<int> nums = {1, 1};
    int ans = 1;

    Solution s;
    REQUIRE(s.maxArea(nums) == ans);
}