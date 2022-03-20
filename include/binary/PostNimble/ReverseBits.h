//
// Created by thera on 3/20/22.
//
//Reverse bits of a given 32 bits unsigned integer.

#ifndef LEETCODEGRIND_REVERSEBITS_H
#define LEETCODEGRIND_REVERSEBITS_H

#include <stdint.h>
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        n = (n >> 16) | (n << 16); // reverse 2 bytes
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8);
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4);
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2);
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1);

        return n;
    }
};

#endif//LEETCODEGRIND_REVERSEBITS_H


// FIRST PASS, WORKING SOLN
//class Solution {
//public:
//    uint32_t reverseBits(uint32_t n) {
//        uint32_t result{};
//        uint8_t sizeOfN = (sizeof(uint32_t) * 8) - 1;
//        for (int i = 0; i <= sizeOfN; i++) {
//            result |= ((n >> i) & 1) << (sizeOfN - i);
//        }
//        return result;
//    }
//};