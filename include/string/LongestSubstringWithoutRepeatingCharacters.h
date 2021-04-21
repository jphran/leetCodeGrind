//Given a string s, find the length of the longest substring without repeating characters.
//
// Created by jfrancis on 4/19/21.
//

#ifndef LEETCODEGRIND_LONGESTSUBSTRINGWITHOUTREPEATINGCHARACTERS_H
#define LEETCODEGRIND_LONGESTSUBSTRINGWITHOUTREPEATINGCHARACTERS_H

#include <string>
#include <map>
#include <unordered_set>

class Solution {
public:
    int lengthOfLongestSubstring(const std::string& s) {
        if(s.empty())
            return 0;

        std::map<char, int> substringMap{};
        int maxSubstringLength = 0;

        for(int front = 0, back = 0; front < s.length(); ++front) {
            if(substringMap.count(s[front]) == 0) {
                substringMap.emplace(s[front], front);
                maxSubstringLength = std::max(maxSubstringLength, (front - back) + 1);
            }
            else {
                back++;
                substringMap.at(s[front]) = front;
            }
        }
        return maxSubstringLength;
    }
};

#endif //LEETCODEGRIND_LONGESTSUBSTRINGWITHOUTREPEATINGCHARACTERS_H
