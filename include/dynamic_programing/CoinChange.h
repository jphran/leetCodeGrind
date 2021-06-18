//
// Created by jfrancis on 3/22/21.
//

#ifndef LEETCODEGRIND_COINCHANGE_H
#define LEETCODEGRIND_COINCHANGE_H

#include <vector>

class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {

        int numCoins = -1;
        std::div_t division;

        for(auto coin : coins){
            division = std::div(amount, coin);
            numCoins += division.quot;
            amount = division.rem;
        }

        return numCoins;
    }
};

#endif //LEETCODEGRIND_COINCHANGE_H
