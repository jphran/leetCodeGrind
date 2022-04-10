"""
https://leetcode.com/problems/alien-dictionary/

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted
lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new
language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes
before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same,
then s is smaller if and only if s.length < t.length.
"""
from typing import Optional


class AlienNode:
    def __init__(self, val: str, before: Optional[set[str]] = None):
        self.val = val
        self.before = before


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # first = AlienNode(val=words[0][0])
        word_graph: dict[str, set[str]] = {}
        for word in words:
            for char in word:
                if char not in word_graph.keys():
                    word_graph[char] = set()
                for node, neighbors in word_graph.items():
                    neighbors.add(word[0])
        return ""
