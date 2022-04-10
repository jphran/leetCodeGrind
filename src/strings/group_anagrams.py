"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1:
            return [strs]

        grouped_anagrams: dict[tuple, list[str]] = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            grouped_anagrams[tuple(sorted_word)].append(word)

        return list(grouped_anagrams.values())
