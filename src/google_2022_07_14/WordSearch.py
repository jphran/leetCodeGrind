"""
Create a class that can store words and then search for them using a basic regex in square brackets. eg.
insert ["abce", "ab", "cat", "abde"] find, "ab" returns ["ab"], find "ab[cd]e" returns ["abce", "abde"]
"""
class Dictionary:
    """class for storing and looking up words."""
    def __init__(self):
        self.lookup: dict[str, Dictionary] = {}
        self.is_terminal = False

    def insert(self, word: str) -> None:
        """Inserts the word into the dictionary."""
        node = self

        for i, c in enumerate(word):
            if c not in node.lookup:
                node.lookup[c] = Dictionary()
            node = node.lookup[c]
            if i == len(word) - 1:
                node.is_terminal = True

    @staticmethod
    def local_search(node: "Dictionary", word_builder: str, pattern: str, results: list[str]) -> None:
        regex = ""
        i = 0
        while i < len(pattern):
            c = pattern[i]
            if c == '[':
                i += 1
                while i < len(pattern) and pattern[i] != ']':
                    regex += pattern[i]
                    i += 1
                i += 1
            if regex:
                for r in regex:
                    Dictionary.local_search(node, word_builder, r + pattern[i:], results)
            if c not in node.lookup:
                return
            node = node.lookup[c]
            word_builder += c
            i += 1

        if node.is_terminal:
            results.append(word_builder)

    def search(self, pattern: str) -> list[str]:
        """Searches for words that match the whole pattern."""
        results: list[str] = []
        word = ""
        Dictionary.local_search(self, word, pattern, results)
        return results


if __name__ == "__main__":
    d = Dictionary()
    d.insert("abcd")
    d.insert("abcde")
    d.insert("abbd")
    d.insert("ab")
    d.insert("abef")
    d.insert("abff")
    d.insert("acdf")
    d.insert("acdfg")
    d.insert("acdg")
    d.insert("abbdf")

    print(f'{d.search("ab")=}')
    assert d.search("ab") == ['ab']
    print(f'{d.search("abc")=}')
    assert d.search("abc") == []
    print(f'{d.search("ab[bc]d")=}')
    assert d.search("ab[bc]d") == ['abbd', 'abcd']
    print(f'{d.search("a[bc][de]f")=}')
    assert d.search("a[bc][de]f") == ['abef', 'acdf']

    print(f'{d.search("a[b][b][d]f")=}')


