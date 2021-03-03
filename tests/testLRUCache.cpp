//
// Created by jfrancis on 3/2/21.
//
#include <catch2/catch.hpp>
#include "LRUCache.h"

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