//
// Created by thera on 10/15/22.
//

#ifndef LEETCODEGRIND_VALIDANAGRAM_H
#define LEETCODEGRIND_VALIDANAGRAM_H

#include <string>
#include <array>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        array<int, 26> first = {0};
        array<int, 26> second = {0};

        for (int i = 0; i < s.size(); i++) {
            auto first_c = s[i];
            auto second_c = t[i];

            first[int(first_c) - int('a')]++;
            second[int(second_c) - int('a')]++;
        }

        return first == second;
    }
};

#endif//LEETCODEGRIND_VALIDANAGRAM_H
