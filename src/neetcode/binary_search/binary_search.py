"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx <= right_idx:
            curr_idx = left_idx + (right_idx - left_idx) // 2
            curr_val = nums[curr_idx]
            if curr_val < target:
                left_idx = curr_idx + 1
            elif curr_val > target:
                right_idx = curr_idx - 1
            else:
                return curr_idx

        return -1
