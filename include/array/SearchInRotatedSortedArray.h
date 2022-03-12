//
// Created by thera on 3/12/22.
//
//There is an integer array nums sorted in ascending order (with distinct values).
//
//Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
// such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
// For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
//
//Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
// or -1 if it is not in nums.
//
//You must write an algorithm with O(log n) runtime complexity.

#ifndef LEETCODEGRIND_SEARCHINROTATEDSORTEDARRAY_H
#define LEETCODEGRIND_SEARCHINROTATEDSORTEDARRAY_H

#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // pre-conditions, trivial case
        if (nums.size() == 1) {
            return nums[0] == target ? 0 : -1;
        }

        int lhs = 0;
        int rhs = (int) nums.size() - 1;
        int mid{};

        while (lhs <= rhs) {
            mid = lhs + (int) floor((rhs - lhs) / 2);

            // exit condition
            if (nums[mid] == target)
                return mid;
            if (nums[lhs] == target)
                return lhs;
            if (nums[rhs] == target)
                return rhs;

            // increment conditions
            if (nums[lhs] < nums[mid]) { // lhs sorted
                if (nums[lhs] < target and target < nums[mid]) // lhs contains target
                    rhs = mid - 1;
                else
                    lhs = mid + 1;
            }
            else { // rhs sorted
                if (nums[mid] < target and target < nums[rhs]) // rhs contains target
                    lhs = mid + 1;
                else
                    rhs = mid - 1;
            }
        }

        // target not found
        return -1;
    }
};

#endif //LEETCODEGRIND_SEARCHINROTATEDSORTEDARRAY_H
