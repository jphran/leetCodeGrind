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
        auto search = mUMap.find(key);
        if(search != mUMap.end()) {
            mKeyList.remove(key);
            mKeyList.push_front(key);
            return search->second;
        } else
            return -1;
    }

    void put(int key, int value) {
        mUMap.insert_or_assign(key, value);
        mKeyList.remove(key);
        mKeyList.push_front(key);
        if(mUMap.size() > mCapacity) {
            mUMap.erase(mKeyList.back());
            mKeyList.pop_back();
        }
    }
private:
    int mCapacity;
    std::list<int>::iterator listIter;
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
//class LRUCache{
//    size_t m_capacity;
//    unordered_map<int,  list<pair<int, int>>::iterator> m_map; //m_map_iter->first: key, m_map_iter->second: list iterator;
//    list<pair<int, int>> m_list;                               //m_list_iter->first: key, m_list_iter->second: value;
//public:
//    LRUCache(size_t capacity):m_capacity(capacity) {
//    }
//    int get(int key) {
//        auto found_iter = m_map.find(key);
//        if (found_iter == m_map.end()) //key doesn't exist
//            return -1;
//        m_list.splice(m_list.begin(), m_list, found_iter->second); //move the node corresponding to key to front
//        return found_iter->second->second;                         //return value of the node
//    }
//    void put(int key, int value) {
//        auto found_iter = m_map.find(key);
//        if (found_iter != m_map.end()) //key exists
//        {
//            m_list.splice(m_list.begin(), m_list, found_iter->second); //move the node corresponding to key to front
//            found_iter->second->second = value;                        //update value of the node
//            return;
//        }
//        if (m_map.size() == m_capacity) //reached capacity
//        {
//            int key_to_del = m_list.back().first;
//            m_list.pop_back();            //remove node in list;
//            m_map.erase(key_to_del);      //remove key in map
//        }
//        m_list.emplace_front(key, value);  //create new node in list
//        m_map[key] = m_list.begin();       //create correspondence between key and node
//    }
//};