//
// Created by thera on 3/20/22.
//
//Given an array nums containing n distinct numbers in the range [0, n],
// return the only number in the range that is missing from the array.

#ifndef LEETCODEGRIND_MISSINGNUMBER_H
#define LEETCODEGRIND_MISSINGNUMBER_H

#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int missingNum = nums.size();

        for (int i = 0; i < nums.size(); i++) {
            missingNum ^= i ^ nums[i];
        }

        return missingNum;
    }
};

#endif//LEETCODEGRIND_MISSINGNUMBER_H


// FIRST PASS, WORKING SOLN
//class Solution {
//public:
//    int missingNumber(vector<int>& nums) {
//        int numsSum{};
//        int sum{};
//
//        for (int i = 0; i < nums.size(); i++) {
//            numsSum += nums[i];
//            sum += i + 1;
//        }
//
//        return sum - numsSum;
//    }
//};