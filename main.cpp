#include <iostream>
#include <map>
#include <vector>
#include <set>

int main() {
    std::multiset<std::pair<int, int>> s;
    for(int i = 0; i < 10; ++i)
      s.insert(std::pair<int, int> (10-i, i * 5));

    for(auto thing : s)
      std::cout << thing.first << "\t" << thing.second << std::endl;
    return 0;
}
