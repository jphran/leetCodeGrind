//
// Created by jfrancis on 4/19/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include <iostream>
#include <vector>
#include "string/LongestSubstringWithoutRepeatingCharacters.h"

TEST_CASE("Given a string, return longest substring without repeating chars."
, "[LongestSubstringWithoutRepeatingChars]") {
    std::string input = "abcabcbb";
    int ans = 3;

    Solution s;
    REQUIRE(s.lengthOfLongestSubstring(input) == ans);
}

TEST_CASE("Given a string, return longest substring without repeating chars1."
, "[LongestSubstringWithoutRepeatingChars]") {
    std::string input = "bbbbbb";
    int ans = 1;

    Solution s;
    REQUIRE(s.lengthOfLongestSubstring(input) == ans);
}

TEST_CASE("Given a string, return longest substring without repeating chars2."
, "[LongestSubstringWithoutRepeatingChars]") {
    std::string input = "pwwkew";
    int ans = 3;

    Solution s;
    REQUIRE(s.lengthOfLongestSubstring(input) == ans);
}

TEST_CASE("Given a string, return longest substring without repeating chars3."
, "[LongestSubstringWithoutRepeatingChars]") {
    std::string input = "";
    int ans = 0;

    Solution s;
    REQUIRE(s.lengthOfLongestSubstring(input) == ans);
}

TEST_CASE("Given a string, return longest substring without repeating chars4."
, "[LongestSubstringWithoutRepeatingChars]") {
    std::string input = "dvdf";
    int ans = 3;

    Solution s;
    REQUIRE(s.lengthOfLongestSubstring(input) == ans);
}

TEST_CASE("Given a string, return longest substring without repeating chars5."
, "[LongestSubstringWithoutRepeatingChars]") {
    std::string input = "tmmzuxt";
    int ans = 5;

    Solution s;
    REQUIRE(s.lengthOfLongestSubstring(input) == ans);
}