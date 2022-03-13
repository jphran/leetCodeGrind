//
// Created by thera on 3/12/22.
//
//You are given an integer array height of length n. There are n vertical lines drawn such that the
// two endpoints of the ith line are (i, 0) and (i, height[i]).
//
//Find two lines that together with the x-axis form a container,
// such that the container contains the most water.
//
//Return the maximum amount of water a container can store.
//
//Notice that you may not slant the container.

#ifndef LEETCODEGRIND_MAXAREA_H
#define LEETCODEGRIND_MAXAREA_H

#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        int width = (int) height.size() - 1;
        int lhs = 0;
        int rhs = width;
        int maxArea = 0;
        int currArea;
        int lhsHeight;
        int rhsHeight;

        for (int i = 0; i < height.size(); ++i) {
            lhsHeight = height[lhs];
            rhsHeight = height[rhs];

            if (lhsHeight < rhsHeight) {
                currArea = lhsHeight * width--;
                lhs++;
            } else {
                currArea = rhsHeight * width--;
                rhs--;
            }

            maxArea = max(currArea, maxArea);
        }
        return maxArea;
    }
};

#endif//LEETCODEGRIND_MAXAREA_H
