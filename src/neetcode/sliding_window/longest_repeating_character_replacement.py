"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1 or k == len(s):
            return len(s)

        lagging_idx = 0
        leading_idx = 0
        freq_dict: dict[str, int] = defaultdict(int)
        highest_freq_character = s[0]
        for leading_idx, character in enumerate(s):
            freq_dict[character] += 1

            if (
                character != highest_freq_character
                and freq_dict[character] > freq_dict[highest_freq_character]
            ):
                highest_freq_character = character

            if (leading_idx - lagging_idx + 1) - freq_dict[highest_freq_character] > k:
                freq_dict[s[lagging_idx]] -= 1
                lagging_idx += 1

        return (leading_idx - lagging_idx) + 1
