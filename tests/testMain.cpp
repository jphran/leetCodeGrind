//
// Created by jfrancis on 2/28/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include <unordered_set>
#include <iostream>

TEST_CASE("x", "[Main]") {
    std::unordered_set<char> mySet{};

    mySet.emplace('c');
    mySet.emplace('b');
    mySet.emplace('a');

    for(auto c : mySet)
        std::cout << c << std::endl;
}