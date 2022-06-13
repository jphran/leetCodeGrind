"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


class Solution:
    def _find_row(self, matrix: list[list[int]], target: int) -> int:
        """Finds and returns the row index that could contain the target."""
        for idx, row in enumerate(matrix):
            if row[0] <= target <= row[-1]:
                return idx

        return -1

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = matrix[self._find_row(matrix, target)]

        if row == -1:
            return False

        # binary search
        left_idx = 0
        right_idx = len(row)

        while left_idx < right_idx:
            idx = left_idx + (right_idx - left_idx) // 2
            val = row[idx]

            if val == target:
                return True
            elif val < target:
                left_idx = idx + 1
            else:
                right_idx = idx

        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 3]]
    target = 3
    print(s.searchMatrix(matrix, target))
