"""
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]+", "", s)
        s = s.lower()
        return s == s[-1 : -len(s) - 1 : -1]


if __name__ == "__main__":
    s = Solution()
    word = "ab_a"
    print(s.isPalindrome(word))
