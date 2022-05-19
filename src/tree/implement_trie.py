"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
from typing import Optional


class Trie:
    def __init__(self, terminal: bool = False):
        self.children: list[Optional[Trie]] = []
        self.is_terminal = terminal

    def insert(self, word: str) -> None:
        if not word:
            return

        parent: Trie = self
        for idx, c in enumerate(word):
            node = parent.children[ord(c) - ord("a")]
            is_terminal = idx == len(word) - 1
            if node is None:
                parent.children[ord(c) - ord("a")] = Trie(is_terminal)

            parent = parent.children[ord(c) - ord("a")]
            if is_terminal:
                parent.is_terminal = is_terminal

    def _search(self, word: str, is_prefix: bool = False):
        if not word:
            return True

        node: Trie = self
        for c in word:
            node = node.children[ord(c) - ord("a")]
            if node is None:
                return False

        if is_prefix:
            return True
        return node.is_terminal

    def search(self, word: str) -> bool:
        return self._search(word)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# WORKING SOLN JUST SLOW AS SHIT
# from typing import Optional, Any


# class TrieNode:
#     def __init__(self, val: str, is_terminal: bool = False):
#         if len(val) != 1 or val is None:
#             raise ValueError
#         self._val = val
#         self._children = [None] * (ord("z") - ord("a") + 1)
#         self._is_terminal = is_terminal
#
#     @property
#     def value(self) -> str:
#         return self._val
#
#     @property
#     def children(self) -> list[Optional[str]]:
#         return self._children
#
#     @property
#     def is_terminal(self) -> bool:
#         return self._is_terminal
#
#     @is_terminal.setter
#     def is_terminal(self, terminal: bool) -> None:
#         self._is_terminal = terminal
#
#     def add_child(self, val: str, terminal: bool = False) -> None:
#         self._children[ord(val) - ord("a")] = TrieNode(val, terminal)
#
#     def get_child(self, val: str) -> Optional[Any]:
#         return self._children[ord(val) - ord("a")]
#
#
# class Trie:
#     _entry_point: list[Optional[TrieNode]]
#     # _lookup: dict[str, int] = {chr(num + ord('a')): num for num in range(ord('z') - ord('a'))}
#
#     def __init__(self):
#         self._entry_point = [None] * (ord("z") - ord("a") + 1)
#
#     def _recursive_insert(self, word: str, node: TrieNode) -> None:
#         if not word:
#             node.is_terminal = True
#             return
#         ch = word[0]
#         if node.get_child(ch) is None:
#             node.add_child(ch, len(word) == 1)
#         self._recursive_insert(word[1:], node.get_child(ch))
#
#     def insert(self, word: str) -> None:
#         if not str:
#             return
#         if self._entry_point[ord(word[0]) - ord("a")] is None:
#             self._entry_point[ord(word[0]) - ord("a")] = TrieNode(
#                 word[0], len(word) == 1
#             )
#
#         self._recursive_insert(word[1:], self._entry_point[ord(word[0]) - ord("a")])
#
#     def _recursive_search(self, word: str, node: TrieNode, full_word: bool) -> bool:
#         if node is None:
#             return False
#         if not word:
#             if full_word:
#                 return node.is_terminal
#             return True
#
#         child = node.get_child(word[0])
#         return self._recursive_search(word[1:], child, full_word)
#
#     def search(self, word: str) -> bool:
#         if not word:
#             return True
#         entry = self._entry_point[ord(word[0]) - ord("a")]
#         if entry is None:
#             return False
#         return self._recursive_search(word[1:], entry, True)
#
#     def startsWith(self, prefix: str) -> bool:
#         if not prefix:
#             return True
#         entry = self._entry_point[ord(prefix[0]) - ord("a")]
#         if entry is None:
#             return False
#         return self._recursive_search(prefix[1:], entry, False)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
