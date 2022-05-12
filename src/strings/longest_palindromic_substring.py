"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def _find_palindrome(self, left: int, right: int, s: str) -> int:
        """
        returns length of the palindrome expanded around the midpoint
        :param left: left index starting at the center of palindrome
        :param right: right index starting at the center of palindrome
        :param s: string to pull palindrome from
        :return: length of palindrome expanded around initial left - right
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # minus one bc centering around a space
        return right - left - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            letter_center = self._find_palindrome(i, i, s)
            space_center = self._find_palindrome(i, i + 1, s)
            palindrome_len = max(letter_center, space_center)
            if palindrome_len > end - start:
                start = i - (palindrome_len - 1) // 2
                end = i + palindrome_len // 2

        return s[start:end + 1]


if __name__ == "__main__":
    s = Solution()
    word = "aabcd"
    print(s.longestPalindrome(word))