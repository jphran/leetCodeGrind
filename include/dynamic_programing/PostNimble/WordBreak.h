//
// Created by thera on 3/28/22.
//
//Given a string s and a dictionary of strings wordDict,
// return true if s can be segmented into a space-separated sequence of one or more dictionary words.
//
//Note that the same word in the dictionary may be reused multiple times in the segmentation.

#ifndef LEETCODEGRIND_WORDBREAK_H
#define LEETCODEGRIND_WORDBREAK_H

#include <vector>
#include <string>
#include <set>

using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        auto sLen = s.size();
        set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<bool> dp(sLen + 1, false);
        dp[0] = true;
        for (int i = 1; i <= sLen; i++) {
            if (dp[i])
                continue;

            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.count(s.substr(j, i - j)) != 0) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[sLen];
    }
};

#endif//LEETCODEGRIND_WORDBREAK_H
