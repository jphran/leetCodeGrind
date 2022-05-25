"""
Given a string s, find the length of the longest substring without repeating characters.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        lagging_idx = 0
        substring_dict: dict[str, int] = defaultdict(int)
        longest_substring = 0
        for leading_idx, character in enumerate(s):
            if character in substring_dict:
                lagging_idx = max(substring_dict[character] + 1, lagging_idx)
            substring_dict[character] = leading_idx
            longest_substring = max(longest_substring, (leading_idx - lagging_idx) + 1)
        return longest_substring
