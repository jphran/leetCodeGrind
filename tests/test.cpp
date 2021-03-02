//
// Created by jfrancis on 2/28/21.
//

#define CATCH_CONFIG_MAIN

#include <iostream>
#include <catch2/catch.hpp>
#include "TwoSum.h"
#include "LRUCache.h"

//********************TWO SUM*************************
TEST_CASE("Given an array of integers nums and an integer target, "
          "return indices of the two numbers such that they add up to target."
          , "[TwoSum]") {

    std::vector<int> nums{2,7,11,15};
    int target = 9;
    std::vector<int> ans{0,1};
    Solution s;

    REQUIRE(s.twoSum(nums, target) == ans);
}

TEST_CASE("Test 2", "[TwoSum]") {
  std::vector<int> nums{3,2,4};
  int target = 6;
  std::vector<int> ans{1,2};
  Solution s;

  REQUIRE(s.twoSum(nums, target) == ans);
}

//********************LRU CACHE*************************
TEST_CASE("LRUCache(int capacity) Initialize the LRU cache with positive size capacity", "[LRU Cache]") {
    int capacity = -3;
    REQUIRE_THROWS_AS(new LRUCache(capacity), std::invalid_argument);
    capacity = 0;
    REQUIRE_THROWS_AS(new LRUCache(capacity), std::invalid_argument);
}

TEST_CASE("LRUCache check basic fn", "[LRU Cache]") {
    int capacity = 3;
    auto* c = new LRUCache(capacity);
    for(int i = 0; i < capacity; ++i) {
        c->put(i, i);
        REQUIRE(c->get(i) == i);
    }
}

TEST_CASE("LRUCache removes oldest elem", "[LRU Cache]") {
    int capacity = 3;
    auto* c = new LRUCache(capacity);
    for(int i = 0; i < capacity + 1; ++i) {
        c->put(i, i);
        REQUIRE(c->get(i) == i);
    }

    REQUIRE(c->get(0) == -1);
}

TEST_CASE("LRUCache updates elem", "[LRU Cache]") {
    int capacity = 3;
    auto* c = new LRUCache(capacity);
    for(int i = 0; i < capacity; ++i) {
        c->put(i, i);
        REQUIRE(c->get(i) == i);
    }

    c->get(0);
    c->put(3,3);

    REQUIRE(c->get(1) == -1);
}

TEST_CASE("LRUCache dups", "[LRU Cached]") {
    int capacity = 2;
    auto* c = new LRUCache(capacity);
    c->put(2,1);
    c->put(2,2);
    REQUIRE(c->get(2) == 2);
}