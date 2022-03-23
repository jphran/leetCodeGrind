//
// Created by thera on 3/20/22.
//
//You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#ifndef LEETCODEGRIND_CLIMBINGSTAIRS_H
#define LEETCODEGRIND_CLIMBINGSTAIRS_H

#include <vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if(n < 3)
            return n;

        vector<int> steps(n + 1, 0);
        steps[0] = 0;
        steps[1] = 1;
        steps[2] = 2;

        for (int i = 3; i <= n; i++) {
            steps[i] = steps[i - 1] + steps[i - 2];
        }
        return steps[n];
    }
};

#endif//LEETCODEGRIND_CLIMBINGSTAIRS_H

// FIRST PASS, TIME OUT, BUT WORKS
//class Solution {
//public:
//    int climbStairs(int n) {
//        return _climbStairs(n);
//    }
//
//    int _climbStairs(int n) {
//        if (n == 2)
//            return 2;
//        if (n == 1)
//            return 1;
//
//        return _climbStairs(n - 1) + _climbStairs(n - 2);
//    }
//};

// SECOND PASS, ACCEPTED using memoization
//class Solution {
//public:
//    int climbStairs(int n) {
//        vector<int> memo(n + 1, 0);
//        return _climbStairs(0, n, memo);
//    }
//
//    int _climbStairs(int step, int n, vector<int>& memo) {
//        if (step == n)
//            return 1;
//        if (step > n)
//            return 0;
//        if (memo.at(step) > 0)
//            return memo[step];
//
//        memo[step] = _climbStairs(step + 1, n, memo) + _climbStairs(step + 2, n, memo);
//
//        return memo[step];
//    }
//};