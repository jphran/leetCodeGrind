//
// Created by jfrancis on 3/5/21.
//

#define CATCH_CONFIG_MAIN

#include "binary/PostNimble/SumOfTwoIntegers.h"
#include <catch2/catch.hpp>
#include <vector>

TEST_CASE("Simple Fn Test sum ints", "[SumOfTwoIntegers]") {
  int a = 1, b = 2, c = 3, d = 4;

  Solution s;
  REQUIRE(s.getSum(a, b) == c);
  REQUIRE(s.getSum(a, c) == d);
}

TEST_CASE("Simple Fn Test sum ints1", "[SumOfTwoIntegers]") {
    int a = -1, b = -2, c = -3;

    Solution s;
    REQUIRE(s.getSum(a, b) == c);
    REQUIRE(s.getSum(b, a) == c);
}

TEST_CASE("Simple Fn Test sum ints2" "[SumOfTwoIntegers]") {
    int a = -1, b = 1, c = 0;

    Solution s;
    REQUIRE(s.getSum(a, b) == c);
    REQUIRE(s.getSum(b, a) == c);
}

TEST_CASE("Simple Fn Test sum ints3" "[SumOfTwoIntegers]") {
    int a = 0, b = 10, c = 10;

    Solution s;
    REQUIRE(s.getSum(a, b) == c);
    REQUIRE(s.getSum(b, a) == c);
}

TEST_CASE("Simple Fn Test sum ints4" "[SumOfTwoIntegers]") {
    int a = INT32_MIN, b = 0, c = INT32_MIN;

    Solution s;
    REQUIRE(s.getSum(a, b) == c);
    REQUIRE(s.getSum(b, a) == c);
}