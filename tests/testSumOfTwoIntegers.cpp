//
// Created by jfrancis on 3/5/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include <vector>
#include "binary/SumOfTwoIntegers.h"

TEST_CASE("Simple Fn Test sum ints", "[SumOfTwoIntegers]") {
  int a = 1, b = 2, c = 3, d = 4;

  Solution s;
  REQUIRE(s.getSum(a, b) == c);
  REQUIRE(s.getSum(a, c) == d);
}