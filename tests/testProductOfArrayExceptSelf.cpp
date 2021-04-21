//
// Created by jfrancis on 4/21/21.
//

#include <catch2/catch.hpp>
#include <vector>
#include "array/ProductOfArrayExceptSelf.h"

TEST_CASE("Given a array, return the result."
, "[ProductOfArrayExceptSelf]") {
    std::vector<int> input = {1, 2, 3, 4};
    std::vector<int> output = {24, 12, 8, 6};

    Solution s;
    REQUIRE(s.productExceptSelf(input) == output);
}

TEST_CASE("Given a array, return the result1."
, "[ProductOfArrayExceptSelf]") {
    std::vector<int> input = {-1, 1, 0, -3, 3};
    std::vector<int> output = {0, 0, 9, 0, 0};

    Solution s;
    REQUIRE(s.productExceptSelf(input) == output);
}

TEST_CASE("Given a array, return the result2."
, "[ProductOfArrayExceptSelf]") {
    std::vector<int> input = {0, 0};
    std::vector<int> output = {0, 0};

    Solution s;
    REQUIRE(s.productExceptSelf(input) == output);
}

TEST_CASE("Given a array, return the result3."
, "[ProductOfArrayExceptSelf]") {
    std::vector<int> input = {0, 4, 0};
    std::vector<int> output = {0, 0, 0};

    Solution s;
    REQUIRE(s.productExceptSelf(input) == output);
}