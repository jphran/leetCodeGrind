"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        num_chars = len(s)
        dp = [1] * num_chars
        longest_so_far = 1
        for i in range(1, num_chars):
            for j in range(i-1, i - 1 - dp[i-1], -1):
                if s[j] == s[i]:
                    break
                dp[i] += 1
            longest_so_far = max(longest_so_far, dp[i])

        return longest_so_far

if __name__ == '__main__':
    s = Solution()
    word = "abcabcbb"
    print(s.lengthOfLongestSubstring(word))