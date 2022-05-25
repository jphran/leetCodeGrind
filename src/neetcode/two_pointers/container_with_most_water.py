"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        left_idx = 0
        right_idx = len(height) - 1

        while left_idx < right_idx:
            left_height = height[left_idx]
            right_height = height[right_idx]
            max_area = max(
                (right_idx - left_idx) * min(left_height, right_height), max_area
            )
            if left_height >= right_height:
                right_idx -= 1
            else:
                left_idx += 1

        return max_area
