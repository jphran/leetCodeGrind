#include <dynamic_programing/PostNimble/LongestIncreasingSubsequence.h>
#include <iostream>


int main() {
    Solution s;
    vector<int> input = {5, 6, 7, 8, 1, 2, 3};
    int ans = s.lengthOfLIS(input);
    std::cout << ans << std::endl;

    return 0;
}
