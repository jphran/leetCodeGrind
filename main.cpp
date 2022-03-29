#include <dynamic_programing/PostNimble/WordBreak.h>
#include <iostream>


int main() {
    Solution s;
//    std::vector<std::string> wordDict = {"cats", "dog", "sand", "and", "cat"};
    std::vector<std::string> wordDict = {"apple", "pen"};


    int ans = s.wordBreak("penapplepen", wordDict);
    std::cout << ans << std::endl;

    return 0;
}
