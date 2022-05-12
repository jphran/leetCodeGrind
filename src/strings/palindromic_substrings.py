"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""


class Solution:
    def _count_palindromes(self, left: int, right: int, s: str) -> int:
        """
        Tally's the number of palindromes centered at right - left.
        :param left:
        :param right:
        :param s:
        :return:
        """
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self._count_palindromes(i, i, s)
            count += self._count_palindromes(i, i + 1, s)

        return count


if __name__ == '__main__':
    s = Solution()
    word = 'abc'
    print(s.countSubstrings(word))
