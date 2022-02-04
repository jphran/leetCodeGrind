#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <unordered_map>


int main() {
    std::set<int> sums{};
    std::vector<int> nums = {20, 20, -1, -1, 20, 20};

    for (auto i : nums) {

    }

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
