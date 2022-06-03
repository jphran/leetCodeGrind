"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # setup local vars for back tracking
        combination_sums: list[list[int]] = []
        curr_combination: list[int] = []

        # sort to prune possible branches
        candidates.sort()

        def back_track(remainder: int) -> None:
            """Simple back tracking to find the combination sums."""
            # base case, soln found
            if remainder == 0:
                combination_sums.append(curr_combination[:])
                return
            # overshot, prune branch
            if remainder < 0:
                return

            for candidate in candidates:
                # TODO
                passk
