//
// Created by jfrancis on 2/27/21.
//

#ifndef LEETCODEGRIND_TWOSUM_H
#define LEETCODEGRIND_TWOSUM_H

#include <vector>

class Solution {
public:
  std::vector<int> twoSum(std::vector<int>& nums, int target);
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