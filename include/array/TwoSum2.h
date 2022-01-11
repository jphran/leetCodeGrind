//
// Created by thera on 9/13/21.
//

#ifndef LEETCODEGRIND_TWOSUM2_H
#define LEETCODEGRIND_TWOSUM2_H

#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> difference{}; //<diff, idx>
        for (int i = 0; i < nums.size(); ++i) {
            int diff = target - nums[i];
            if (difference.count(diff) != 0)
                return {difference[diff], i};
            difference.emplace(nums[i], i);
        }
        return {-1}; // big fail
    }
};

#endif //LEETCODEGRIND_TWOSUM2_H
