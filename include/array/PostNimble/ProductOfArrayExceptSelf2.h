//
// Created by thera on 1/11/22.
//

#ifndef LEETCODEGRIND_PRODUCTOFARRAYEXCEPTSELF2_H
#define LEETCODEGRIND_PRODUCTOFARRAYEXCEPTSELF2_H

#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result (nums.size());

        result[0] = 1;
        for (auto i = 1; i < nums.size(); ++i) {
            result[i] = nums[i - 1] * result[i - 1];
        }

        int prodFromRight = 1;
        for (auto i = nums.size() - 1; i > 0; --i) {
            prodFromRight *= nums[i];
            result[i - 1] *= prodFromRight;
        }

        return result;
    }
};

#endif //LEETCODEGRIND_PRODUCTOFARRAYEXCEPTSELF2_H
