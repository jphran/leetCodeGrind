"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq
import itertools
from collections import Counter


class Solution:
    # WORKING BUCKET SORT SOLN
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)

        buckets = [[] for _ in range(len(nums))]
        for value, freq in count.items():
            buckets[freq - 1].append(value)

        flat_buckets = list(itertools.chain(*buckets))
        return flat_buckets[-k:]

    # WORKING HEAP SOLN
    # def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    #     if k == len(nums):
    #         return nums
    #
    #     count = Counter(nums)
    #
    #     return heapq.nlargest(n=k, iterable=count.keys(), key=lambda key: count[key])
