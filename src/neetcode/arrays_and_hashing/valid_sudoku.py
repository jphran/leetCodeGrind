"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        valid_row: list[set[int]] = [set() for _ in range(9)]
        valid_col: list[set[int]] = [set() for _ in range(9)]
        valid_square: list[set[int]] = [set() for _ in range(9)]

        for i in range(len(board)):
            row_square = (i // 3) * 3
            for j in range(len(board[i])):
                col_square = j // 3
                curr_val = board[i][j]
                if curr_val == ".":
                    continue
                curr_val = int(curr_val)
                if (
                    curr_val in valid_square[row_square + col_square]
                    or curr_val in valid_col[j]
                    or curr_val in valid_row[i]
                ):
                    return False
                valid_square[row_square + col_square].add(curr_val)
                valid_row[i].add(curr_val)
                valid_col[j].add(curr_val)

        return True


# class Solution:
#     def isValidSudoku(self, board: list[list[str]]) -> bool:
#         valid_row: list[list[int]] = [[] for _ in range(9)]
#         valid_col: list[list[int]] = [[] for _ in range(9)]
#         valid_square: list[list[int]] = [[] for _ in range(9)]
#
#         for i in range(9):
#             valid_row[i] = [0] * 9
#             valid_col[i] = [0] * 9
#             valid_square[i] = [0] * 9
#
#         for i in range(len(board)):
#             row_square = (i // 3) * 3
#             for j in range(len(board[i])):
#                 col_square = j // 3
#                 curr_val = board[i][j]
#                 if curr_val == ".":
#                     continue
#                 curr_val = int(curr_val)
#                 idx = curr_val - 1
#                 if (
#                     valid_square[row_square + col_square][idx] != 0
#                     or valid_col[j][idx] != 0
#                     or valid_row[i][idx] != 0
#                 ):
#                     return False
#                 valid_square[row_square + col_square][idx] = curr_val
#                 valid_row[i][idx] = curr_val
#                 valid_col[j][idx] = curr_val
#
#         return True
