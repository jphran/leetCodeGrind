//
// Created by thera on 10/13/22.
//

#ifndef LEETCODEGRIND_HAPPYNUMBER_H
#define LEETCODEGRIND_HAPPYNUMBER_H

using namespace std;

#include <set>
#include <cmath>

class Solution {
private:
    static int nextNum(int n) {
        int sum = 0;
        while (n > 0) {
            auto res = div(n, 10);
            n = res.quot;
            sum += int(pow(res.rem, 2));
        }
        return sum;
    }
public:
    bool isHappy(int n) {
        set<int> visited{n};
        while (n != 1) {
            n = nextNum(n);
            if (visited.count(n) != 0) {
                return false;
            }
            visited.insert(n);
        }
        return true;
    }
};


#endif//LEETCODEGRIND_HAPPYNUMBER_H
