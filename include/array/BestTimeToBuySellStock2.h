//
// Created by thera on 1/10/22.
//

#ifndef LEETCODEGRIND_BESTTIMETOBUYSELLSTOCK2_H
#define LEETCODEGRIND_BESTTIMETOBUYSELLSTOCK2_H

using namespace std;

#include <limits>

class Solution {
private:
    uint16_t mLowestPrice{};
    uint16_t mMaxProfit{};

public:
    int maxProfit(vector<int>& prices) {
        mLowestPrice = numeric_limits<uint16_t>::max();
        mMaxProfit = 0;
        for (auto p : prices) {
            if (p < mLowestPrice) {
                mLowestPrice = p;
            }
            else if (p - mLowestPrice > mMaxProfit) {
                mMaxProfit = p - mLowestPrice;
            }
        }
        return mMaxProfit;
    }
};

#endif //LEETCODEGRIND_BESTTIMETOBUYSELLSTOCK2_H
