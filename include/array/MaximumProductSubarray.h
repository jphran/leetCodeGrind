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
        int init = nums[0];
        int min_prod = init;
        int max_prod = init;
        int best = init;

        for (int i = 1; i < nums.size(); i++) {
            int num = nums[i];
            int tmp_max = max(num, max(min_prod * num, max_prod * num));
            min_prod = min(num, min(min_prod * num, max_prod * num));
            max_prod = tmp_max;
            best = max(max_prod, best);
        }
        return best;
    }
};

#endif //LEETCODEGRIND_MAXIMUMPRODUCTSUBARRAY_H
