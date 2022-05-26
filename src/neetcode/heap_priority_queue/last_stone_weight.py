"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""
import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        if len(stones) <= 1:
            return stones[0] if stones else 0

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            larger_stone = heapq.heappop(stones)
            smaller_stone = heapq.heappop(stones)
            result_stone = larger_stone - smaller_stone
            if result_stone < 0:
                heapq.heappush(stones, result_stone)

        return -stones[0] if stones else 0
