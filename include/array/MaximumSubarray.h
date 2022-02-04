//
// Created by thera on 2/3/22.
//

#ifndef LEETCODEGRIND_MAXIMUMSUBARRAY_H
#define LEETCODEGRIND_MAXIMUMSUBARRAY_H

#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // nums is guaranteed to have at least 1 element
        int currentMax = 0;
        int bestMax = INT_MIN;
        for (auto n : nums) {
            currentMax = max(n, currentMax + n);
            bestMax = max(currentMax, bestMax);
        }

        return bestMax;
    }
};

#endif //LEETCODEGRIND_MAXIMUMSUBARRAY_H
