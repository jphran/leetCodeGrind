//
// Created by thera on 3/22/22.
//
//You are given an integer array coins representing coins of different denominations and an
// integer amount representing a total amount of money.
//Return the fewest number of coins that you need to make up that amount.
// If that amount of money cannot be made up by any combination of the coins, return -1.
//You may assume that you have an infinite number of each kind of coin.

#ifndef LEETCODEGRIND_COINCHANGE_H
#define LEETCODEGRIND_COINCHANGE_H

#include <vector>

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> count(amount + 1, amount + 1);
        count[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    count[i] = min(count[i], count[i - coin] + 1);
                }
            }
        }
        return count[amount] < amount + 1 ? count[amount] : -1;
    }
};

#endif//LEETCODEGRIND_COINCHANGE_H
