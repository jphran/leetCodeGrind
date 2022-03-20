//Given a string s and a dictionary of strings wordDict, return true if s can be segmented
//into a space-separated sequence of one or more dictionary words.
//
//Note that the same word in the dictionary may be reused multiple times in the segmentation.

//Constraints:
//
//1 <= s.length <= 300
//1 <= wordDict.length <= 1000
//1 <= wordDict[i].length <= 20
//s and wordDict[i] consist of only lowercase English letters.
//All the strings of wordDict are unique.


//
// Created by jfrancis on 4/21/21.
//

#ifndef LEETCODEGRIND_WORDBREAK_H
#define LEETCODEGRIND_WORDBREAK_H

#include <string>
#include <vector>
#include <unordered_map>
#include <map>
#include <list>

class Solution {
public:
    bool wordBreak(const std::string& s, std::vector<std::string>& wordDict) {
        std::unordered_map<int, std::list<int>> posMap{};

        for(const auto& word : wordDict) {
            size_t pos = s.find(word, 0);
            while(pos != std::string::npos) {
                std::list<int> endPos = {int(pos + word.length())};
                if(posMap.count(pos) != 0) {
                    endPos.splice(endPos.begin(), posMap.at(pos));
                    posMap.at(pos) = endPos;
                }
                else {
                    posMap.emplace(pos, endPos);
                }
                pos = s.find(word, pos + 1);
            }
        }



        return true;
    }

private:
    bool canCreate(const std::list<int>& endPos, int currPos, int strLength) {
        for(int pos : endPos) {

        }
    }
};

#endif //LEETCODEGRIND_WORDBREAK_H
