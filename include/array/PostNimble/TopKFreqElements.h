//
// Created by thera on 10/15/22.
//

#ifndef LEETCODEGRIND_TOPKFREQELEMENTS_H
#define LEETCODEGRIND_TOPKFREQELEMENTS_H

#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counter{};
        for (int & num : nums) {
            counter[num]++;
        }

        vector<pair<int, int>> maxHeap{};
        for (auto kvPair : counter) {
            maxHeap.emplace_back(pair<int, int>{kvPair.second, kvPair.first});
        }
        make_heap(maxHeap.begin(), maxHeap.end());

        vector<int> result{};
        for (int i = 0; i < k; i++) {
            result.push_back(maxHeap.front().second);
            pop_heap(maxHeap.begin(), maxHeap.end());
            maxHeap.pop_back();
        }

        return result;
    }
};

#endif//LEETCODEGRIND_TOPKFREQELEMENTS_H
