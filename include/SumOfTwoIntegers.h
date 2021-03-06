//
// Created by jfrancis on 3/5/21.
//

//Given two integers a and b,
//return the sum of the two integers without using the operators + and -.

#ifndef LEETCODEGRIND_SUMOFTWOINTEGERS_H
#define LEETCODEGRIND_SUMOFTWOINTEGERS_H

class Solution {
public:
  int getSum(int a, int b) {
    int sum = 0;
    bool carry = false;
    bool isOne;
    bool first;
    bool second;
    uint8_t bitmask = 0x01;

    for(int i = 0; i < sizeof(a) * 8; ++i) {
      first = a & (1 << i);
      second = b & (1 << i);
      isOne = ((first ^ second) ^ carry);
      if(isOne)
        sum |= (1 << i);
      else
        sum &= ~(1 << i);
      carry = ((first ^ second) & carry) | (first & second);
    }

    return sum;
  }
};

#endif // LEETCODEGRIND_SUMOFTWOINTEGERS_H
