//
// Created by jfrancis on 3/8/21.
//

#define CATCH_CONFIG_MAIN

#include "dynamic_programing/PostSarcos/ClimbingStairs.h"
#include <catch2/catch.hpp>

//********************LRU CACHE*************************
TEST_CASE("basic fn test for climbing stairs", "[ClimbingStairs]") {
    int stairs = 2;
    int waysToClimb = 2;
    Solution s;
    REQUIRE(s.climbStairs(stairs) == waysToClimb);
}
TEST_CASE("basic fn test for climbing stairs1", "[ClimbingStairs]") {
    int stairs = 3;
    int waysToClimb = 3;
    Solution s;
    REQUIRE(s.climbStairs(stairs) == waysToClimb);
}
TEST_CASE("basic fn test for climbing stairs2", "[ClimbingStairs]") {
    int stairs = 4;
    int waysToClimb = 5;
    Solution s;
    REQUIRE(s.climbStairs(stairs) == waysToClimb);

//    stairs = 45;
//    waysToClimb = 1134903170;
//    REQUIRE(s.climbStairs(stairs) == waysToClimb);
}

