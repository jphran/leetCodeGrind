"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in counter.items():
            buckets[count].append(num)

        top_k_frequent: list[int] = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k_frequent.append(num)
                if len(top_k_frequent) == k:
                    return top_k_frequent

        return []

    # WORKING max heap based on num count O(NlogK)
    # def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    #     count = Counter(nums)
    #
    #     return heapq.nlargest(n=k, iterable=count.keys(), key=lambda key: count[key])


if __name__ == "__main__":
    s = Solution()
    nums = [1, 0, 0, 3]
    k = 1
    print(s.topKFrequent(nums, k))
