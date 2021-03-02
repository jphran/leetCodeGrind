//
// Created by jfrancis on 3/1/21.
//

#ifndef LEETCODEGRIND_LRUCACHE_H
#define LEETCODEGRIND_LRUCACHE_H

#include <unordered_map>
#include <list>

class LRUCache {
public:
    explicit LRUCache(int capacity){
        if(capacity > 0)
            mCapacity = capacity;
        else
            throw std::invalid_argument("Capacity must be positive");
    }

    int get(int key) {
        auto search = mUMap.find(key);  //O(log n)
        if(search != mUMap.end()) {
            mKeyList.remove(key);  // O(n)
            mKeyList.push_front(key);
            return search->second;
        } else
            return -1;
    }

    void put(int key, int value) {
        mUMap.insert_or_assign(key, value);  // O(log n)
        mKeyList.remove(key);  // O(n)
        mKeyList.push_front(key);
        if(mUMap.size() > mCapacity) {
            mUMap.erase(mKeyList.back());  // O(log n)
            mKeyList.pop_back();
        }
    }
private:
    int mCapacity;
    std::unordered_map<int, int> mUMap;
    std::list<int> mKeyList;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

#endif //LEETCODEGRIND_LRUCACHE_H
