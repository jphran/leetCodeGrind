//You are given an array prices where prices[i]
//is the price of a given stock on the ith day.
//You want to maximize your profit by choosing a
//single day to buy one stock and choosing a different
//day in the future to sell that stock.
//Return the maximum profit you can achieve from
//this transaction. If you cannot achieve any profit, return 0.

//
// Created by jfrancis on 3/3/21.
//

#ifndef LEETCODEGRIND_BESTTIMETOBUYSELLSTOCK_H
#define LEETCODEGRIND_BESTTIMETOBUYSELLSTOCK_H

#include <vector>

class Solution {
private:
  uint16_t mMinPrice;
  uint16_t mMaxProfit;

public:
  int maxProfit(std::vector<int>& prices) {
    mMinPrice = INT16_MAX;
    mMaxProfit = 0;

    for(auto price : prices) {
      if(price < mMinPrice)
        mMinPrice = price;
      else if(price - mMinPrice > mMaxProfit)
        mMaxProfit = price - mMinPrice;
    }

    return mMaxProfit;
  }
};

#endif // LEETCODEGRIND_BESTTIMETOBUYSELLSTOCK_H


// Community soln uses kadane's algo (max subarray algo)
// which accounts for negative sums duh