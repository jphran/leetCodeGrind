//
// Created by jfrancis on 4/22/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include <vector>
#include <string>
#include "dynamic_programing/WordBreak.h"

TEST_CASE("Given a word dict and a string, "
          "return true if string consists of whole words in dict",
          "[WordBreak]") {
    std::string str = "leetcode";
    std::vector<std::string> wordDict = {"leet","code"};
    bool ans = true;

    Solution s;
    REQUIRE(s.wordBreak(str, wordDict) == ans);
}

TEST_CASE("Given a word dict and a string, "
          "return true if string consists of whole words in dict1",
          "[WordBreak]") {
    std::string str = "catsandog";
    std::vector<std::string> wordDict = {"cats","dog","sand","and","cat"};
    bool ans = false;

    Solution s;
    REQUIRE(s.wordBreak(str, wordDict) == ans);
}

TEST_CASE("Given a word dict and a string, "
          "return true if string consists of whole words in dict2",
          "[WordBreak]") {
    std::string str = "applepenapple";
    std::vector<std::string> wordDict = {"apple", "pen"};
    bool ans = true;

    Solution s;
    REQUIRE(s.wordBreak(str, wordDict) == ans);
}

TEST_CASE("Given a word dict and a string, "
          "return true if string consists of whole words in dict3",
          "[WordBreak]") {
    std::string str = "cars";
    std::vector<std::string> wordDict = {"car", "ca", "rs"};
    bool ans = true;

    Solution s;
    REQUIRE(s.wordBreak(str, wordDict) == ans);
}