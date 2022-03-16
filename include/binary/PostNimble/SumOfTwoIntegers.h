//
// Created by thera on 3/15/22.
//
//Given two integers a and b, return the sum of the two integers without using the operators + and -.

#ifndef LEETCODEGRIND_SUMOFTWOINTEGERS_H
#define LEETCODEGRIND_SUMOFTWOINTEGERS_H

class Solution {
public:
    int getSum(int a, int b) {
        int sum{};

        do {
            sum = a ^ b;
            b = ((unsigned)(a & b) << 1);
            a = sum;
        } while (b);
        return sum;
    }
};

#endif//LEETCODEGRIND_SUMOFTWOINTEGERS_H
