//
// Created by thera on 3/15/22.
//
//Given two integers a and b, return the sum of the two integers without using the operators + and -.

#ifndef LEETCODEGRIND_SUMOFTWOINTEGERS_H
#define LEETCODEGRIND_SUMOFTWOINTEGERS_H

class Solution {
public:
    int getSum(int a, int b) {
        int tmp{};

        do {
            tmp = a ^ b;
            b = ((unsigned)(a & b) << 1);
            a = tmp;
        } while (b);
        return a;
    }
};

#endif//LEETCODEGRIND_SUMOFTWOINTEGERS_H
