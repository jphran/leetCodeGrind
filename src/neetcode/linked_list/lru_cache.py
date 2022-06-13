"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""
from typing import Any


class DNode:
    def __init__(
        self, key: int, value: int, prev: Any | None = None, next_: Any | None = None
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity

        # setup hashmap
        self._cache: dict[int, DNode] = {}

        # setup doubly linked list
        self._tail = DNode(0, -1)
        self._head = DNode(0, -1, next_=self._tail)
        self._tail.prev = self._head

    def _remove_node(self, key: int | None = None) -> None:
        node = self._cache[key]
        # patch list
        node.prev.next = node.next
        node.next.prev = node.prev
        # delete node from cache and list
        del node
        del self._cache[key]

    def _move_node_to_mru(self, key: int, value: int) -> None:
        node = self._cache[key]
        node.value = value

        # patch list
        node.prev.next = node.next
        node.next.prev = node.prev

        # move node behind head
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node

    def _add_node(self, key: int, value: int) -> None:
        new_node = DNode(key=key, value=value, prev=self._head, next_=self._head.next)

        # add to doubly linked list
        self._head.next.prev = new_node
        self._head.next = new_node

        # add to cache
        self._cache[key] = new_node

    def get(self, key: int) -> int:
        val = self._cache.get(key, self._head).value

        if val != -1:
            self._move_node_to_mru(key, val)

        return val

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._move_node_to_mru(key, value)
        else:
            self._add_node(key, value)
            if len(self._cache) > self._capacity:
                self._remove_node(self._tail.prev.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
