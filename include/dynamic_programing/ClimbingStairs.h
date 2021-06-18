//You are climbing a staircase. It takes n steps to reach the top.
//Each time you can either climb 1 or 2 steps. In how many distinct
//ways can you climb to the top?

//
// Created by jfrancis on 3/8/21.
//

#ifndef LEETCODEGRIND_CLIMBINGSTAIRS_H
#define LEETCODEGRIND_CLIMBINGSTAIRS_H

// fibonacci dynamic programming approach
class Solution {
public:
    static int climbStairs(int n) {
        if(n == 1)
            return 1;

        int waysToClimb[n];
        waysToClimb[0] = 1;
        waysToClimb[1] = 2;

        for(int i = 2; i < n; ++i) {
            waysToClimb[i] = waysToClimb[i - 1] + waysToClimb[i - 2];
        }

        return waysToClimb[n-1];
    }
};

#endif //LEETCODEGRIND_CLIMBINGSTAIRS_H


// fibonacci dynamic programming approach
//class Solution {
//public:
//    static int climbStairs(int n) {
//        if(n == 1)
//            return 1;
//
//        int waysToClimb[n];
//        waysToClimb[0] = 1;
//        waysToClimb[1] = 2;
//
//        for(int i = 2; i < n; ++i) {
//            waysToClimb[i] = waysToClimb[i - 1] + waysToClimb[i - 2];
//        }
//
//        return waysToClimb[n-1];
//    }
//};

// my first recursive soln, too slow
//class Solution {
//private:
//    int climbStairsRecursive(int n){
//        switch(n) {
//            case 1:
//                return 1;
//            case 2:
//                return 2;
//            default:
//                return climbStairsRecursive(n - 1) + climbStairsRecursive(n - 2);
//        }
//    }
//public:
//    int climbStairs(int n) {
//        return climbStairsRecursive(n);
//    }
//};