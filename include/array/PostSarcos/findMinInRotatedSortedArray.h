//
// Created by thera on 3/8/22.
//

#ifndef LEETCODEGRIND_FINDMININROTATEDSORTEDARRAY_H
#define LEETCODEGRIND_FINDMININROTATEDSORTEDARRAY_H

#include <vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        // trivial array, return only elem
        if (nums.size() == 1)
            return nums[0];
        // array is sorted, first elem is min
        if (nums[0] < nums[nums.size() - 1])
            return nums[0];

        int lhs = 0;
        int rhs = (int)nums.size() - 1;
        int mid{};
        while (lhs <= rhs - 1) {
            mid = lhs + (int)floor((rhs - lhs) / 2);
            // exit conditions
            if (nums[mid] > nums[mid + 1])
                return nums[mid + 1];
            if (nums[mid] < nums[mid - 1])
                return nums[mid];

            // increment, determine which half contains min
            if (nums[mid] < nums[lhs] or nums[mid] < nums[rhs])
                rhs = mid - 1;
            else
                lhs = mid + 1;
        }
        return nums[mid];
    }
};

#endif //LEETCODEGRIND_FINDMININROTATEDSORTEDARRAY_H


// My initial, working soln
//class Solution {
//public:
//    int findMin(vector<int>& nums) {
//        if (nums.size() == 1)
//            return nums[0];
//        if (nums.size() == 2)
//            return min(nums[0], nums[1]);
//
//        // modified binary search
//        int lhsIdx = 0;
//        int rhsIdx = nums.size() - 1;
//        int centerIdx = rhsIdx / 2;
//        int lhs = nums[lhsIdx];
//        int rhs = nums[rhsIdx];
//        int center = nums[centerIdx];
//        int curr_min{};
//
//        while (centerIdx != lhsIdx and centerIdx != rhsIdx) {
//            curr_min = min(min(lhs, center), rhs);
//
//            if (curr_min == lhs or curr_min == center) {
//                rhsIdx = centerIdx;
//                centerIdx = (rhsIdx + lhsIdx) / 2;
//            }
//            else {
//                lhsIdx = centerIdx;
//                centerIdx = (rhsIdx + centerIdx) / 2;
//            }
//
//            lhs = nums[lhsIdx];
//            rhs = nums[rhsIdx];
//            center = nums[centerIdx];
//        }
//        return min(min(lhs, center), rhs);
//    }
//};