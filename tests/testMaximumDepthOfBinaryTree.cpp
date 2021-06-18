//
// Created by jfrancis on 4/21/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include <vector>
#include "tree/MaximumDepthOfBinaryTree.h"

TEST_CASE("Given a tree, return the height."
, "[MaximumDepthOfBinaryTree]") {
    TreeNode fifteen(15);
    TreeNode seven(7);
    TreeNode twenty(20, &fifteen, &seven);

    TreeNode nine(9);

    TreeNode root(3, &nine, &twenty);

    int ans = 3;

    Solution s;
    REQUIRE(s.maxDepth(&root) == ans);
}

TEST_CASE("Given a tree, return the height1."
, "[MaximumDepthOfBinaryTree]") {
    TreeNode two(2);

    TreeNode root(3, nullptr, &two);

    int ans = 2;

    Solution s;
    REQUIRE(s.maxDepth(&root) == ans);
}

TEST_CASE("Given a tree, return the height2."
, "[MaximumDepthOfBinaryTree]") {
    int ans = 0;

    Solution s;
    REQUIRE(s.maxDepth(nullptr) == ans);
}

TEST_CASE("Given a tree, return the height3."
, "[MaximumDepthOfBinaryTree]") {
    TreeNode root(0);
    int ans = 1;

    Solution s;
    REQUIRE(s.maxDepth(&root) == ans);
}