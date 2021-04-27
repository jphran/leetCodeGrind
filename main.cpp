#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <unordered_map>

enum CLOTHES {
    JEANS = 0,
    SHOES,
    SKIRTS,
    TOPS
};

int main() {
    std::vector<int> prices = {3, 4, 5, 2, 1};
    std::set<int> priceSet(prices.begin(), prices.end());
    auto pointer = priceSet.upper_bound(5);

    int num = 0;
    while(pointer != priceSet.end()) {
        num++;
        pointer++;
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
