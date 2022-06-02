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
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # init local vars
        curr_combination: list[int] = []
        combination_sums: list[list[int]] = []

        # sort candidates so, we can cut down the number of decision branches
        candidates.sort()

        def back_track(idx: int, remaining: int) -> None:
            """Back track any unique repeating combination that reaches target"""
            # soln found
            if remaining == 0:
                combination_sums.append(curr_combination[:])
                return
            # non-reachable path
            if remaining < 0:
                return

            # try branching
            for i in range(idx, len(candidates)):
                curr_combination.append(candidates[i])
                back_track(i, remaining - candidates[i])
                curr_combination.pop()

        back_track(0, target)

        return combination_sums

    # WORKING SOLN 5/21/22
    # def _back_track(
    #     self,
    #     candidates: list[int],
    #     target: int,
    #     curr_idx: int,
    #     curr_combination: list[int],
    #     result: list[list[int]],
    # ) -> None:
    #     if target == 0:
    #         result.append(curr_combination.copy())
    #         return
    #     if target < 0:
    #         return
    #
    #     for i in range(curr_idx, len(candidates)):
    #         curr_combination.append(candidates[i])
    #         self._back_track(
    #             candidates, target - candidates[i], i, curr_combination, result
    #         )
    #         curr_combination.pop()
    #
    # def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
    #     results = []
    #
    #     self._back_track(candidates, target, 0, [], results)
    #
    #     return results
