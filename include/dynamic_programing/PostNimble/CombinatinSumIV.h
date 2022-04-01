//
// Created by thera on 4/1/22.
//
//Given an array of distinct integers nums and a target integer target,
// return the number of possible combinations that add up to target.
//
//The test cases are generated so that the answer can fit in a 32-bit integer.

#ifndef LEETCODEGRIND_COMBINATINSUMIV_H
#define LEETCODEGRIND_COMBINATINSUMIV_H

#include <map>
#include <vector>

class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        auto memo = map<int, int>{};
        return _combinationSum4(nums, target, 0, memo);
    }

    int _combinationSum4(vector<int>& nums, int target, int currSum, map<int, int>& memo) {
        if (currSum == target)
            return 1;

        int combination {};
        int thisSum{};
        for (int i = 0; i < nums.size(); i++) {
            thisSum = currSum + nums[i];
            if (memo.count(thisSum) != 0) {
                combination += memo[thisSum];
                continue;
            }
            if (thisSum <= target) {
                memo[thisSum] = _combinationSum4(nums, target, thisSum, memo);
                combination += memo[thisSum];
            }
        }

        return combination;
    }
};

#endif//LEETCODEGRIND_COMBINATINSUMIV_H
