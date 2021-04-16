//
// Created by jfrancis on 3/22/21.
//

#include <catch2/catch.hpp>
#include <iostream>

#include "CoinChange.h"

TEST_CASE("basic fn test for coin change", "[CoinChange]") {
    std::vector<int> coins = {1, 2, 5};
    int amount = 11;
    int ans = 3;

    Solution s;
    int output = s.coinChange(coins, amount);
    REQUIRE(output == ans);
}
