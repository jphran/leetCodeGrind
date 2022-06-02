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
    def __init__(self, is_terminal: bool = False):
        self.children: list[Optional[Trie]] = [None] * (ord("z") - ord("a") + 1)
        self.is_terminal = is_terminal

    def insert(self, word: str) -> None:
        node = self
        for idx, s in enumerate(word):
            if node.children[ord(s) - ord("a")] is None:
                node.children[ord(s) - ord("a")] = Trie()
            node = node.children[ord(s) - ord("a")]
            if idx == len(word) - 1:
                node.is_terminal = True

    def _search(self, word: str, require_terminal: bool) -> bool:
        node = self
        for s in word:
            if node.children[ord(s) - ord("a")] is None:
                return False
            node = node.children[ord(s) - ord("a")]
        return node.is_terminal if require_terminal else True

    def search(self, word: str) -> bool:
        return self._search(word, True)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix, False)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
