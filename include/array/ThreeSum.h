//
// Created by thera on 3/12/22.
//
//Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
// such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
//
//Notice that the solution set must not contain duplicate triplets.

#ifndef LEETCODEGRIND_THREESUM_H
#define LEETCODEGRIND_THREESUM_H

#include <set>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int> &nums) {
        // pre-conditions
        if (nums.size() < 3)
            return {};

        // pre-sort for pointer use O(nlogn)
        std::sort(nums.begin(), nums.end());

        int sum;
        int pivotVal;
        vector<vector<int>> solutionVectorsVector;

        for (int pivot = 0; pivot < nums.size() and nums[pivot] <= 0; pivot++) {
            pivotVal = nums[pivot];
            int lhs = pivot + 1;
            int rhs = (int) nums.size() - 1;
            int lhsVal;
            int rhsVal;

            if (pivot == 0 or nums[pivot] != nums[pivot - 1]) {
                while (lhs < rhs) {
                    sum = pivotVal + nums[lhs] + nums[rhs];
                    if (sum == 0) {
                        lhsVal = nums[lhs++];
                        rhsVal = nums[rhs--];
                        solutionVectorsVector.push_back({pivotVal, lhsVal, rhsVal});
                        // avoid duplicates
                        while (lhs < rhs and nums[lhs] == nums[lhs - 1])
                            ++lhs;
                    } else if (sum > 0) {
                        --rhs;
                    } else {
                        ++lhs;
                    }
                }
            }
        }
        return solutionVectorsVector;
    }
};

#endif//LEETCODEGRIND_THREESUM_H
