"""
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window. If there is no such substring,
return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = {ch: t.count(ch) for ch in t}
        found: list[tuple[int, str]] = []

        start_idx = 0
        while s[start_idx] not in required:
            start_idx += 1
            if start_idx == len(s):
                return ""

        left_pointer = start_idx
        right_pointer = start_idx

        for i in range(start_idx, len(s)):
            curr_char = s[i]
            if curr_char in required:
                required[curr_char] -= 1
                found.append((i, curr_char))
                while required.get(s[left_pointer], 1) < 0:
                    found.remove((left_pointer, s[left_pointer]))
                    required[s[left_pointer]] += 1
                    left_pointer = found[0][0]
                right_pointer = i

        return (
            s[left_pointer : right_pointer + 1]
            if all(val <= 0 for val in required.values())
            else ""
        )


if __name__ == "__main__":
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s, t))
