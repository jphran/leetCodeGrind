"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations: list[list[int]] = []
        curr_perm: list[int] = []

        def back_track(candidates: list[int]) -> None:
            """Simple back tracking to find permutations."""
            if len(curr_perm) == len(nums):
                permutations.append(curr_perm[:])
                return

            for i in range(len(candidates)):
                curr_num = candidates.pop(0)
                curr_perm.append(curr_num)
                back_track(candidates)
                curr_perm.pop()
                candidates.append(curr_num)

        back_track(nums[:])

        return permutations
