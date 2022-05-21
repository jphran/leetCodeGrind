"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""


class Solution:
    def _back_track(
        self,
        candidates: list[int],
        target: int,
        curr_idx: int,
        curr_combination: list[int],
        result: list[list[int]],
    ) -> None:
        if target == 0:
            result.append(curr_combination.copy())
            return
        if target < 0:
            return

        for i in range(curr_idx, len(candidates)):
            curr_combination.append(candidates[i])
            self._back_track(
                candidates, target - candidates[i], i, curr_combination, result
            )
            curr_combination.pop()

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        self._back_track(candidates, target, 0, [], results)

        return results
