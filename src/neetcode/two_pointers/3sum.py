"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


"""


class Solution:
    def _two_sum(self, nums: list[int], start: int, results: list[list[int]]) -> None:
        left_idx = start + 1
        right_idx = len(nums) - 1
        while left_idx < right_idx:
            three_sum = nums[start] + nums[left_idx] + nums[right_idx]
            if three_sum == 0:
                results.append([nums[start], nums[left_idx], nums[right_idx]])
                left_idx += 1
                right_idx -= 1
                while left_idx < right_idx and nums[left_idx] == nums[left_idx - 1]:
                    left_idx += 1
            elif three_sum > 0:
                right_idx -= 1
            else:
                left_idx += 1

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        three_sum: list[list[int]] = []
        for idx, n in enumerate(nums):
            if n > 0:
                break
            if idx == 0 or nums[idx] != nums[idx - 1]:
                self._two_sum(nums, idx, three_sum)

        return three_sum
