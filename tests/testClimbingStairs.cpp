//
// Created by jfrancis on 3/8/21.
//
#include <catch2/catch.hpp>
#include "ClimbingStairs.h"

//********************LRU CACHE*************************
TEST_CASE("basic fn test for climbing stairs", "[ClimbingStairs]") {
    int stairs = 2;
    int waysToClimb = 2;
    Solution s;
    REQUIRE(s.climbStairs(stairs) == waysToClimb);

    stairs = 3;
    waysToClimb = 3;
    REQUIRE(s.climbStairs(stairs) == waysToClimb);

    stairs = 4;
    waysToClimb = 5;
    REQUIRE(s.climbStairs(stairs) == waysToClimb);

//    stairs = 45;
//    waysToClimb = 1134903170;
//    REQUIRE(s.climbStairs(stairs) == waysToClimb);
}

