"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # setup local vars
        subsets: list[list[int]] = []
        curr_subset: list[int] = []
        # sort nums so we can easily prune duplicate subsets
        nums.sort()

        def back_track(idx: int) -> None:
            """Simple back tracking for finding subsets w/out duplicates in an array that may contain duplicates."""
            # base case, idx out of range, save found soln, pop stack
            if idx == len(nums):
                subsets.append(curr_subset[:])
                return

            # include curr num in the soln
            curr_subset.append(nums[idx])
            back_track(idx + 1)
            # skip dups
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            # exclude curr num in the soln
            curr_subset.pop()
            back_track(idx + 1)

        back_track(0)

        return subsets
