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
        if(get(key) != -1) {
            mUMap.insert_or_assign(key, value);  // O(log n)
            return;
        }
        else {
            mUMap.insert(key, value);
            mKeyList.push_front(key);
        }
        if (mUMap.size() > mCapacity) {
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




// ********* COMMUNITY SOLN, O(1) list + umap implementation ************
//class LRUCache {
//public:
//
//    int size;
//    list<int> lru;                              // MRU ... LRU
//    unordered_map<int, list<int>::iterator> mp; // key -> iterator
//    unordered_map<int, int> kv;
//
//    LRUCache(int capacity) {
//        size=capacity;
//    }
//
//    int get(int key) {
//        if (kv.count(key) == 0) return -1;
//        updateLRU(key);
//        return kv[key];
//    }
//
//    void put(int key, int value) {
//        if (kv.size() == size && kv.count(key) == 0)
//            evict();
//        updateLRU(key);
//        kv[key] = value;
//    }
//
//    void updateLRU(int key) {
//        if (kv.count(key))
//            lru.erase(mp[key]);
//        lru.push_front(key);
//        mp[key] = lru.begin();
//    }
//
//    void evict() {
//        mp.erase(lru.back());
//        kv.erase(lru.back());
//        lru.pop_back();
//    }
//
//
//};