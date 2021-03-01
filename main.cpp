#include <iostream>
#include <TwoSum.h>

int main() {
    std::vector<int> nums{3,2,4};
    Solution s;
    auto vals = s.twoSum(nums, 6);
    std::cout << vals[0] << vals[1] << std::endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
