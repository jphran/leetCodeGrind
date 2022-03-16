//
// Created by justi on 12/16/2021.
//

#ifndef LEETCODEGRIND_MAXPROFIT_2021_12_16_H
#define LEETCODEGRIND_MAXPROFIT_2021_12_16_H

#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mCurrSubArrayProfit = 0;
        int mMaxSubArrayProfit = 0;

        for (int i = 1; i < prices.size(); ++i) {
            mCurrSubArrayProfit += prices[i] - prices[i - 1];
            mCurrSubArrayProfit = max(0, mCurrSubArrayProfit);
            mMaxSubArrayProfit = max(mCurrSubArrayProfit, mMaxSubArrayProfit);
        }

        return mMaxSubArrayProfit;
    }
};

#endif //LEETCODEGRIND_MAXPROFIT_2021_12_16_H
