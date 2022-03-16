//Given an integer array nums, return an array answer such that answer[i] is equal to the
//product of all the elements of nums except nums[i].
//The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
//
// Created by jfrancis on 4/21/21.
//

#ifndef LEETCODEGRIND_PRODUCTOFARRAYEXCEPTSELF_H
#define LEETCODEGRIND_PRODUCTOFARRAYEXCEPTSELF_H

#include <vector>
#include <set>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int total = 0;
        std::set<int> zeroIndices{};

        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i] != 0) {
                if(total != 0)
                    total *= nums[i];
                else
                    total = nums[i];
            }
            else {
                zeroIndices.emplace(i);
            }
        }

        std::vector<int> result(nums.size(), 0);
        for(int i = 0; i < nums.size(); ++i) {
            if(not zeroIndices.empty()) {
                if (zeroIndices.size() > 1)
                    break;
                else if(zeroIndices.count(i) != 0)
                    result.at(i) = total;
            }
            else {
                result.at(i) = (total / nums[i]);
            }
        }

        return result;
    }
};

#endif //LEETCODEGRIND_PRODUCTOFARRAYEXCEPTSELF_H
