//Given an array nums containing n distinct numbers in the range [0, n],
//return the only number in the range that is missing from the array.
//
//Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
//
// Created by jfrancis on 4/21/21.
//

#ifndef LEETCODEGRIND_MISSINGNUMBER_H
#define LEETCODEGRIND_MISSINGNUMBER_H

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int missingNum = nums.size();
        for(int i = 0; i < nums.size(); ++i) {
            missingNum ^= i ^ nums[i];
        }

        return missingNum;
    }
};

#endif //LEETCODEGRIND_MISSINGNUMBER_H
