#include <binary/PostNimble/NumberOfOneBits.h>


int main() {
    Solution s;
    s.hammingWeight(11);

    return 0;
}

//int sum = 0;
//bool carry = false;
//bool first;
//bool second;
//uint8_t bitmask = 0x01;
//for(int i = 0; i < sizeof(a) * 8; ++i) {
//first = a & (1 << i);
//second = b & (1 << i);
//bool isOne = ((first ^ second) ^ carry);
//if(isOne)
//sum |= (1 << i);
//else
//sum &= ~(1 << i);
//carry = ((first ^ second) & carry) | (first & second);
//}
