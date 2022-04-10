"""
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution:
    _udlr = {'u': [0, 1], 'd': [0, -1], 'l': [-1, 0], 'r': [1, 0]}

    def exist(self, board: list[list[str]], word: str) -> bool:
        visited: set[tuple[int, int]] = set()
        for row, line in enumerate(board):
            for col, letter in enumerate(line):
                if self._backtrack_exists(start=[row, col], word=word, visited=visited, board=board):
                    return True
        return False

    def _backtrack_exists(self, start: list[int], word: str, visited: set[tuple[int, int]],
                          board: list[list[str]]) -> bool:
        if len(word) == 0:
            return True

        x = start[0]
        y = start[1]

        if (
                x < 0 or x >= len(board)
                or y < 0 or y >= len(board[0])
                or (x, y) in visited
                or board[x][y] != word[0]
        ):
            return False

        visited.add((x, y))

        result = False
        for x_offset, y_offset in self._udlr.values():
            result = self._backtrack_exists(start=[x + x_offset, y + y_offset],
                                            word=word[1:], visited=visited, board=board)
            if result:
                break

        visited.remove((x, y))

        return result


if __name__ == '__main__':
    s = Solution()
    board = [['a', 'a']]
    word = 'aaa'
    print(s.exist(board, word))
