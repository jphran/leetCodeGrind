//
// Created by thera on 3/24/22.
//
//Given an integer array nums, return the length of the longest strictly increasing subsequence.
//A subsequence is a sequence that can be derived from an array by deleting some or no elements
// without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence
// of the array [0,3,1,6,2,2,7].

#ifndef LEETCODEGRIND_LONGESTINCREASINGSUBSEQUENCE_H
#define LEETCODEGRIND_LONGESTINCREASINGSUBSEQUENCE_H

#include <vector>
using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int> &nums) {
        vector<int> lis(nums.size(), 1);
        int result = 1;
        for (int i = 1; i < nums.size(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i] and lis[j] >= lis[i]) {
                    lis[i] = lis[j] + 1;
                    result = max(result, lis[i]);
                }
            }
        }

        return result;
    }
};

#endif//LEETCODEGRIND_LONGESTINCREASINGSUBSEQUENCE_H
