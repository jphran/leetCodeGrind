//
// Created by jfrancis on 3/22/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>

#include "dynamic_programing/PostNimble/CoinChange.h"

TEST_CASE("basic fn test for coin change", "[CoinChange]") {
    std::vector<int> coins = {1, 2, 5};
    int amount = 11;
    int ans = 3;

    Solution s;
    int output = s.coinChange(coins, amount);
    REQUIRE(output == ans);
}

TEST_CASE("basic fn test for coin change1", "[CoinChange]") {
    std::vector<int> coins = {2};
    int amount = 3;
    int ans = -1;

    Solution s;
    int output = s.coinChange(coins, amount);
    REQUIRE(output == ans);
}

TEST_CASE("basic fn test for coin change2", "[CoinChange]") {
    std::vector<int> coins = {1};
    int amount = 0;
    int ans = 0;

    Solution s;
    int output = s.coinChange(coins, amount);
    REQUIRE(output == ans);
}

TEST_CASE("failed test for coin change", "[CoinChange]") {
    std::vector<int> coins = {186, 419, 83, 408};
    int amount = 6249;
    int ans = 20;

    Solution s;
    int output = s.coinChange(coins, amount);
    REQUIRE(output == ans);
}
