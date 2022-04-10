"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
from collections import deque


class Solution:
    _matches = {"}": "{", "]": "[", ")": "("}

    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = deque()
        stack.append("a")

        for ch in s:
            if ch in self._matches:
                if stack.pop() != self._matches[ch]:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 1
