"""
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)

        longest_run = 0
        for num in num_set:
            if num - 1 in num_set:
                continue

            curr_run = 1
            while num + 1 in num_set:
                num += 1
                curr_run += 1

            longest_run = max(longest_run, curr_run)

        return longest_run
