//
// Created by thera on 1/11/22.
//

#ifndef LEETCODEGRIND_CONTAINSDUPLICATE_H
#define LEETCODEGRIND_CONTAINSDUPLICATE_H

#include <set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> num_set{};
        for (auto n : nums) {
            auto ret = num_set.insert(n);
            if (not ret.second) {
                return true;
            }
        }
        return false;
    }
};

#endif //LEETCODEGRIND_CONTAINSDUPLICATE_H
