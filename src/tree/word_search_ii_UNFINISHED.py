"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class TrieNode:
    letter: str
    links: dict
    # links: Optional[dict] = None

    @staticmethod
    def create(letter: str, links: list):
        return TrieNode(letter=letter, links={node.letter: node for node in links})


class Solution:
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    board: dict[
        str,
    ]

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        for y in board:
            for x in y:
                links = []
                for x_bump, y_bump in self.neighbors:
                    new_y = y + y_bump
                    new_x = x + x_bump
                    if (new_x < 0 or new_x > len(y)) or (
                        new_y < 0 or new_y > len(board)
                    ):
                        continue


if __name__ == "__main__":
    nodes = [TrieNode("a"), TrieNode("z")]
    node = TrieNode.create("a", nodes)
    print("hello")
