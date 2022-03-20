//
// Created by thera on 3/20/22.
//
//Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
// ans[i] is the number of 1's in the binary representation of i.


#ifndef LEETCODEGRIND_COUNTINGBITS_H
#define LEETCODEGRIND_COUNTINGBITS_H

#include <vector>
using namespace std;

class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans{};
        ans.reserve(n);
        int numBits{};

        for (int i = 0; i <= n; ++i) {
            numBits = 0;
            for (int j = 0; j < sizeof(int) * 8; ++j) {
                if ((i >> j) & 1) {
                    numBits++;
                }
            }
            ans.push_back(numBits);
        }

        return ans;
    }
};

#endif//LEETCODEGRIND_COUNTINGBITS_H


// FIRST PASS, WORKING SOLN
//class Solution {
//public:
//    vector<int> countBits(int n) {
//        vector<int> ans{};
//        ans.reserve(n);
//
//        for (int i = 0; i <= n; ++i) {
//            ans.push_back(__builtin_popcount(i));
//        }
//
//        return ans;
//    }
//};