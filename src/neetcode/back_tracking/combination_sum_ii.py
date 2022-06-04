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
    def _back_track(
        self,
        curr_combination: list[int],
        idx: int,
        remainder: int,
        candidates: list[int],
        combination_sums: list[list[int]],
    ) -> None:
        """Simple back tracking to find the combination sums."""
        # base case, soln found
        if remainder == 0:
            combination_sums.append(curr_combination[:])
            return
        # prune dead branch
        if remainder < 0:
            return

        while idx < len(candidates):
            curr_combination.append(candidates[idx])
            self._back_track(
                curr_combination,
                idx + 1,
                remainder - candidates[idx],
                candidates,
                combination_sums,
            )
            idx += 1
            while idx < len(candidates) and candidates[idx] == candidates[idx - 1]:
                idx += 1
            curr_combination.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # setup local vars for back tracking
        combination_sums: list[list[int]] = []
        curr_combination: list[int] = []

        # sort to prune possible branches
        candidates.sort()

        self._back_track(curr_combination, 0, target, candidates, combination_sums)

        return combination_sums
