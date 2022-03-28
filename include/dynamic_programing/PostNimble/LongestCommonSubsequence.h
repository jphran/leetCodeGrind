//
// Created by thera on 3/27/22.
//
//Given two strings text1 and text2, return the length of their longest common subsequence.
// If there is no common subsequence, return 0.
//A subsequence of a string is a new string generated from the original string with some
// characters (can be none) deleted without changing the relative order of the remaining characters.
//For example, "ace" is a subsequence of "abcde".
//A common subsequence of two strings is a subsequence that is common to both strings.

#ifndef LEETCODEGRIND_LONGESTCOMMONSUBSEQUENCE_H
#define LEETCODEGRIND_LONGESTCOMMONSUBSEQUENCE_H

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> memo{};
        return lcsRecursive(text1, text2, memo);
    }

    int lcsRecursive(string text1, string text2, vector<vector<int>>& memo) {
        if (text1.empty() or text2.empty())
            return 0;

        char first = text1[0];
        int i;
        for (i = 0; i < text2.size(); i++) {
            if (first == text2[i]) {
                break;
            }
        }
        int soln1{};
        if (i < text2.size())
            soln1 = lcsRecursive(text1.substr(1), text2.substr(i + 1), memo) + 1;
        int soln2 = lcsRecursive(text1.substr(1), text2, memo);
        return max(soln1, soln2);
    }
};

#endif//LEETCODEGRIND_LONGESTCOMMONSUBSEQUENCE_H
