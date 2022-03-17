//
// Created by thera on 3/17/22.
//

#ifndef LEETCODEGRIND_NUMBEROFONEBITS_H
#define LEETCODEGRIND_NUMBEROFONEBITS_H

#include <cstdint>

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count{};
        for (int i = 0; i < sizeof(uint32_t) * 8; i++ ) {
            count += (n >> i) & 1 ? 1 : 0;
        }
        return count;
    }
};

#endif//LEETCODEGRIND_NUMBEROFONEBITS_H

// FIRST TRY SUCCESS, NOW OPTIMIZE
//class Solution {
//public:
//    int hammingWeight(uint32_t n) {
//        int count{};
//        for (int i = 0; i < sizeof(uint32_t) * 8; i++ ) {
//            count += (n >> i) & 1 ? 1 : 0;
//        }
//        return count;
//    }
//};

// MY SECOND ATTEMPT AT OPTIMIZATION, SUCKED WAY HARDER.
//class Solution {
//public:
//    int hammingWeight(uint32_t n) {
//        if (n == 0) {
//            return 0;
//        }
//        if (n == 1) {
//            return 1;
//        }
//
//        int count{};
//        int lessOne = n - 1;
//        while (n > 0) {
//            n ^= (n & ~lessOne);
//            lessOne = n - 1;
//            count++;
//        }
//        return count;
//    }
//};