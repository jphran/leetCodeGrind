"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    _matches = {"]": "[", "}": "{", ")": "("}

    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for c in s:
            if c in self._matches:
                if len(stack) == 0:
                    return False
                last_paren = stack.pop(-1)
                if last_paren != self._matches[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
