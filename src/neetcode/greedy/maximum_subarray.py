"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
import sys


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        max_sum = -sys.maxsize

        for num in nums:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_sum
