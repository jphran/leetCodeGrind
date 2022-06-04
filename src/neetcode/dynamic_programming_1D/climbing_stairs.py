"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:

1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # trivial soln
        if n == 1:
            return n

        n_minus_1 = 2
        n_minus_2 = 1
        for i in range(2, n):
            i = n_minus_2 + n_minus_1
            n_minus_2 = n_minus_1
            n_minus_1 = i

        return n_minus_1
