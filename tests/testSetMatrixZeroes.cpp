//
// Created by jfrancis on 4/19/21.
//

#include <catch2/catch.hpp>
#include "SetMatrixZeroes.h"
#include <iostream>
#include <vector>

TEST_CASE("Given a matrix, set row and columns of zero to zero."
, "[SetMatrixZeroes]") {
    std::vector<std::vector<int>> input = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
    std::vector<std::vector<int>> ans = {{0,0,0,0}, {0,4,5,0},{0,3,1,0}};
    Solution s;
    s.setZeroes(input);
    REQUIRE(input == ans);
}

TEST_CASE("Given a matrix, set row and columns of zero to zero1."
, "[SetMatrixZeroes]") {
    std::vector<std::vector<int>> input = {{1,1,1},{1,0,1},{1,1,1}};
    std::vector<std::vector<int>> ans = {{1,0,1},{0,0,0},{1,0,1}};
    Solution s;
    s.setZeroes(input);
    REQUIRE(input == ans);
}

TEST_CASE("Given a matrix, set row and columns of zero to zero2."
, "[SetMatrixZeroes]") {
    std::vector<std::vector<int>> input = {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
    std::vector<std::vector<int>> ans = {{0,0,0,0},{0,4,5,0},{0,3,1,0}};
    Solution s;
    s.setZeroes(input);
    REQUIRE(input == ans);
}