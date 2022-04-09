"""
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        turn_zero: list[list[int]] = []
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    turn_zero.append([i, j])

        for i, j in turn_zero:
            matrix[i] = [0] * num_cols
            for x in range(0, num_rows):
                matrix[x][j] = 0
