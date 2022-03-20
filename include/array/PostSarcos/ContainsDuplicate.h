//
// Created by jfrancis on 7/20/21.
//

//Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
//
//
//
//Example 1:
//
//Input: nums = [1,2,3,1]
//Output: true
//
//Example 2:
//
//Input: nums = [1,2,3,4]
//Output: false
//
//Example 3:
//
//Input: nums = [1,1,1,3,3,4,3,2,4,2]
//Output: true
//
//
//
//Constraints:
//
//1 <= nums.length <= 105
//-109 <= nums[i] <= 109
//


#ifndef LEETCODEGRIND_CONTAINSDUPLICATE_H
#define LEETCODEGRIND_CONTAINSDUPLICATE_H

#include <vector>
#include <set>

class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::set<int> numSet;
        bool result = false;
        for(auto num : nums) {
            if (numSet.count(num) == 0)
                numSet.emplace(num);
            else {
                result = true;
                break;
            }
        }

        return result;
    }
};

#endif //LEETCODEGRIND_CONTAINSDUPLICATE_H