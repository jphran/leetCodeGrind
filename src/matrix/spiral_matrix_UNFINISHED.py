"""
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        num_rows = len(matrix)
        if num_rows == 1:
            return matrix[0]

        num_cols = len(matrix[0])
        if num_cols == 1:
            return [x[0] for x in matrix]

        r = num_rows - 1
        c = num_cols - 1

        spiral_order: list[int] = []

        num_rings = min(num_rows, num_cols) + 1 // 2

        for ring in range(num_rings + 1):
            # left to right include end points
            spiral_order.extend(matrix[ring][ring : num_cols - ring])

            if len(spiral_order) >= num_cols * num_rows:
                return spiral_order

            # top to bottom exclude endpoints
            for y in range(ring + 1, r - ring):
                spiral_order.append(matrix[y][c - ring])

            if len(spiral_order) >= num_cols * num_rows:
                return spiral_order

            # right to left, include end points
            spiral_order.extend(matrix[r - ring][-1 - ring : -num_cols - 1 - ring : -1])

            if len(spiral_order) >= num_cols * num_rows:
                return spiral_order

            # bottom to top exclude endpoints
            for y in range(r - ring - 1, ring, -1):
                spiral_order.append(matrix[y][ring])

            if len(spiral_order) >= num_cols * num_rows:
                return spiral_order

        return spiral_order


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(s.spiralOrder(matrix))
