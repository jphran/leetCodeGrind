"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""


class WordDictionary:
    def __init__(self, terminal: bool = False):
        self.links = {}
        self.terminal = terminal

    def addWord(self, word: str) -> None:
        if not word:
            return

        node = self
        for idx, c in enumerate(word):
            terminal = idx == len(word) - 1
            if c not in node.links:
                node.links[c] = WordDictionary(terminal)
            node = node.links[c]
            if terminal:
                node.terminal = terminal

    def search(self, word: str) -> bool:
        if not word:
            return self.terminal

        node = self
        for idx, c in enumerate(word):
            if c == ".":
                for link in node.links.values():
                    if link.search(word[idx + 1 :]):
                        return True
                return False

            if c not in node.links:
                return False
            node = node.links[c]

        return node.terminal


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
