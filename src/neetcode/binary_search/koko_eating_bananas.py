"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""
from math import ceil


class Solution:
    @staticmethod
    def _time_to_eat(piles: list[int], k: int) -> int:
        if k <= 0:
            raise ValueError(f"{k=} too low")

        time_to_eat = 0
        for pile in piles:
            # ceil cause koko needs to finish
            time_to_eat += ceil(pile / k)
        return time_to_eat

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # trivial
        if len(piles) == 1:
            return ceil(piles[0] / h)

        min_k = 1
        max_k = max(piles)

        # binary search, if size of search space is 0, break
        while min_k < max_k:
            # floor to find min
            k = (max_k + min_k) // 2
            time_to_eat = self._time_to_eat(piles, k)
            print(f"{min_k=}, {k=}, {max_k=}, {time_to_eat=}")

            # how to reduce the search space took the longest bc instead of returning k when time_to_eat == h,
            # we need to return the minimum k that satisfies time_to_eat <= h
            if time_to_eat > h:  # invalid soln, k is definitely not min_k, so increment
                min_k = k + 1
            else:  # possibly valid soln, so do not remove k from search space
                max_k = k

        return min_k
