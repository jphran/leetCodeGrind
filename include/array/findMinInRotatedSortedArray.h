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
        if (nums.size() == 1)
            return nums[0];
        if (nums.size() == 2)
            return min(nums[0], nums[1]);

        // modified binary search
        int lhsIdx = 0;
        int rhsIdx = nums.size() - 1;
        int centerIdx = rhsIdx / 2;
        int lhs = nums[lhsIdx];
        int rhs = nums[rhsIdx];
        int center = nums[centerIdx];
        int curr_min{};

        while (centerIdx != lhsIdx and centerIdx != rhsIdx) {
            curr_min = min(min(lhs, center), rhs);

            if (curr_min == lhs or curr_min == center) {
                rhsIdx = centerIdx;
                centerIdx = (rhsIdx + lhsIdx) / 2;
            }
            else {
                lhsIdx = centerIdx;
                centerIdx = (rhsIdx + centerIdx) / 2;
            }

            lhs = nums[lhsIdx];
            rhs = nums[rhsIdx];
            center = nums[centerIdx];
        }
        return min(min(lhs, center), rhs);
    }
};

#endif //LEETCODEGRIND_FINDMININROTATEDSORTEDARRAY_H
