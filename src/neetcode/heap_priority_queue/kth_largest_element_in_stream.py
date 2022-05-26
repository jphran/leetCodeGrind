"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self._k = k
        # probably want to copy, so we don't get wrecked by external mods
        heapq.heapify(nums)
        self._heap = nums

        while len(self._heap) > k:
            heapq.heappop(self._heap)

    def add(self, val: int) -> int:
        heapq.heappush(self._heap, val)
        if len(self._heap) > self._k:
            heapq.heappop(self._heap)
        return self._heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
