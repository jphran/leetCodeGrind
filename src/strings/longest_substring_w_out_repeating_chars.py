"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        char_map: dict[str, int] = {s[0]: 0}  # {'char': idx}
        longest_so_far = 1
        j = 0
        for i in range(1, len(s)):
            ch = s[i]
            if ch in char_map and char_map[ch] >= j:
                j = char_map[ch] + 1
                char_map[ch] = i
            else:
                char_map[ch] = i
                longest_so_far = max(longest_so_far, (i - j) + 1)
        return longest_so_far


if __name__ == '__main__':
    s = Solution()
    word = "abcabcbb"
    print(s.lengthOfLongestSubstring(word))