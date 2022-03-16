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
        int max_prod = init;
        int min_prod = init;
        int best_prod = init;
        int tmp{};
        int num{};

        for (int i = 1; i < nums.size(); i++) {
            num = nums[i];
            tmp = max(max(max_prod * num, min_prod * num), num);
            min_prod = min(min(max_prod * num, min_prod * num), num);
            max_prod = tmp;

            best_prod = max(max_prod, best_prod);
        }

        return best_prod;
    }
};

#endif //LEETCODEGRIND_MAXIMUMPRODUCTSUBARRAY_H
