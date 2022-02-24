//
// Created by thera on 2/23/22.
//
// Problem:
// Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
// The test cases are generated so that the answer will fit in a 32-bit integer.
// A subarray is a contiguous subsequence of the array.

#ifndef LEETCODEGRIND_MAXIMUMPRODUCTSUBARRAY_H
#define LEETCODEGRIND_MAXIMUMPRODUCTSUBARRAY_H

#include <vector>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int best_prod = INT32_MIN;
        int prod = 1;
        int running_prod = prod;
        for (int num : nums) {
            int tmp_prod = prod * num;
            if (tmp_prod > prod)
                prod = tmp_prod;
            else
                prod = num;
            best_prod = max(best_prod, prod);
        }

        return best_prod;
    }
};

#endif //LEETCODEGRIND_MAXIMUMPRODUCTSUBARRAY_H
