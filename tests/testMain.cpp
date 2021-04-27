//
// Created by jfrancis on 2/28/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include <unordered_set>
#include <iostream>
#include <chrono>

class Timer
{
private:
    // Type aliases to make accessing nested type easier
    using clock_t = std::chrono::high_resolution_clock;
    using second_t = std::chrono::duration<double, std::ratio<1> >;

    std::chrono::time_point<clock_t> m_beg;

public:
    Timer() : m_beg(clock_t::now())
    {
    }

    void reset()
    {
        m_beg = clock_t::now();
    }

    double elapsed() const
    {
        return std::chrono::duration_cast<second_t>(clock_t::now() - m_beg).count();
    }
};

int fibSeq(int n, std::vector<int>& memo) {
    if(memo.size() > n)
        return memo.at(n);
    int result = fibSeq(n - 1, memo) + fibSeq(n - 2, memo);
    memo.emplace_back(result);
    return result;
}

TEST_CASE("x", "[Main]") {
    std::vector<int> memoization = {0, 1, 1};

    Timer t;
    for(int i = 0; i < 40; ++i) {
        fibSeq(i, memoization);
    }
    std::cout << fibSeq(20, memoization) << std::endl;
    std::cout << t.elapsed() << std::endl;
}

int naiveFibSeq(int n) {
    if(n == 0)
        return 0;
    if(n <= 2)
        return 1;

   return naiveFibSeq(n - 1) + naiveFibSeq(n - 2);
}

TEST_CASE("x1", "[Main]") {
    Timer t;
    for(int i = 0; i < 40; ++i) {
        naiveFibSeq(i);
    }
    std::cout << naiveFibSeq(20) << std::endl;
    std::cout << t.elapsed() << std::endl;
}