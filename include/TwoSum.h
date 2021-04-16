//
// Created by jfrancis on 2/27/21.
//

#ifndef LEETCODEGRIND_TWOSUM_H
#define LEETCODEGRIND_TWOSUM_H

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        for (int i = 0; i <= nums.size(); ++i) {
            int first = nums.at(i);
            for (int j = i + 1; j < nums.size(); ++j) {
                if (first + nums.at(j) == target)
                    return {i, j};
            }
        }
        return {};
    }
};


#endif //LEETCODEGRIND_TWOSUM_H


// ********** JAVA SOLN, ONE PASS HASH TABLE ************
//public int[] twoSum(int[] nums, int target) {
//    Map<Integer, Integer> map = new HashMap<>();
//    for (int i = 0; i < nums.length; i++) {
//        int complement = target - nums[i];
//        if (map.containsKey(complement)) {
//            return new int[] { map.get(complement), i };
//        }
//        map.put(nums[i], i);
//    }
//    throw new IllegalArgumentException("No two sum solution");
//}