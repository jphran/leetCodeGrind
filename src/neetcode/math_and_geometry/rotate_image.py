"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x_max = len(matrix[0]) - 1
        y_max = len(matrix) - 1
        n = len(matrix)

        for y in range(0, (n // 2) + n % 2):
            for x in range(y, x_max - y):
                tmp = matrix[y][x]

                # rotate bottom left to top left
                matrix[y][x] = matrix[y_max - x][y]
                # rotate bottom right to bottom left
                matrix[y_max - x][y] = matrix[y_max - y][x_max - x]
                # rotate top right to bottom right
                matrix[y_max - y][x_max - x] = matrix[x][x_max - y]
                # rotate top left to top right
                matrix[x][x_max - y] = tmp

        return matrix

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.rotate(matrix))