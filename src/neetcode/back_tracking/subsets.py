"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # init my local vars
        curr_subset: list[int] = []
        subsets: list[list[int]] = []

        def back_track(stopping_length: int) -> None:
            """Back tracks the unique, non-repeating subsets."""
            # stopping criteria
            if stopping_length >= len(nums):
                subsets.append(curr_subset[:])
                return

            # include current num in soln
            curr_subset.append(nums[stopping_length])
            back_track(stopping_length + 1)
            # exclude current num in soln
            curr_subset.pop()
            back_track(stopping_length + 1)

        back_track(0)

        return subsets
