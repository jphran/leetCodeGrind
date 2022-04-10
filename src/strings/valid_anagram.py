"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.
"""
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_in_s: dict[str, int] = defaultdict(int)
        letters_in_t: dict[str, int] = defaultdict(int)

        for i in range(len(s)):
            letters_in_t[t[i]] += 1
            letters_in_s[s[i]] += 1

        return letters_in_t == letters_in_s


# WORKING FIRST SOLN, time to optimize
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         s = sorted(s, key=lambda x: x[0])
#         t = sorted(t, key=lambda x: x[0])
#
#         for i in range(len(s)):
#             if s[i] != t[i]:
#                 return False
#
#         return True
