"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # no trivial list strs

        grouped_anagrams: dict[tuple[int], list[str]] = defaultdict(list)
        for s in strs:  # O(N)
            counter = [0] * (ord("z") - ord("a") + 1)
            for c in s:  # O(K)
                counter[ord(c) - ord("a")] += 1
            grouped_anagrams[tuple(counter)].append(s)

        # total O(NK)
        return list(grouped_anagrams.values())

    # WORKING NKlogK soln, let's optimize
    # def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    #     # no trivial list strs
    #
    #     grouped_anagrams: dict[str, list[str]] = defaultdict(list)
    #     for s in strs:  # O(N)
    #         grouped_anagrams[str(sorted(s))].append(s)  # O(KlogK)
    #
    #     # total O(NKlogK)
    #     return list(grouped_anagrams.values())
