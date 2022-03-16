//
// Created by jfrancis on 3/3/21.
//

#define CATCH_CONFIG_MAIN

#include "array/PostNimble/BestTimeToBuySellStock2.h"
#include <catch2/catch.hpp>
#include <vector>

TEST_CASE("Simple Fn Test stock", "[BestTimeToBuySellStock]") {
  std::vector<int> prices = {7,1,5,3,6,4};
  int ans = 5;

  Solution s;
  REQUIRE(s.maxProfit(prices) == ans);
}

TEST_CASE("stock 2", "[BestTimeToBuySellStock]") {
  Solution s;

  std::vector<int> prices = {7,6,4,3,1};
  int ans = 0;
  REQUIRE(s.maxProfit(prices) == ans);
}

TEST_CASE("stock 3", "[BestTimeToBuySellStock]") {
  Solution s;

  std::vector<int> prices = {2,4,1};
  int ans = 2;
  REQUIRE(s.maxProfit(prices) == ans);
}

TEST_CASE("stock 4", "[BestTimeToBuySellStock]") {
    Solution s;

    std::vector<int> prices = {3,2,6,5,0,3};
    int ans = 4;
    REQUIRE(s.maxProfit(prices) == ans);
}