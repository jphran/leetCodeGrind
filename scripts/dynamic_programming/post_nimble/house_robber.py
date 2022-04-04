# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money
# you can rob tonight without alerting the police.

# TODO: solve using DP

# WORKING RECURSIVE SOLN W MEMO
class Solution(object):
    _memo: list[int]

    def __init__(self):
        pass

    def rob(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        self._memo = [-1] * len(nums)
        return self._recursive_rob(0, nums)

    def _recursive_rob(self, idx: int, nums: list[int]) -> int:
        """
        Recursive rob.
        :param nums:
        :return:
        """
        # base case
        if idx >= len(nums):
            return 0

        # we've seen it before
        if self._memo[idx] != -1:
            return self._memo[idx]

        # find max of curr idx in soln and curr idx not in soln.
        idx_in_soln = self._recursive_rob(idx=idx + 2, nums=nums) + nums[idx]
        idx_not_in_soln = self._recursive_rob(idx=idx + 1, nums=nums)
        self._memo[idx] = max(idx_in_soln, idx_not_in_soln)
        return self._memo[idx]

if __name__ == '__main__':
    s = Solution()
    nums = [2, 1, 1, 2]
    print(s.rob(nums))