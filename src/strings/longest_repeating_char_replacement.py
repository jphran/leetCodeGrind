"""
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        if length <= 1 or k == length:
            return length

        left_pointer = 0
        freq_map: dict[str, int] = {s[0]: 1}  # {'char': freq}
        highest_freq_char = s[0]
        right_pointer = 0

        for right_pointer in range(1, length):
            curr_char = s[right_pointer]

            if curr_char not in freq_map:
                freq_map[curr_char] = 0
            freq_map[curr_char] += 1

            if (
                curr_char != highest_freq_char
                and freq_map[curr_char] >= freq_map[highest_freq_char]
            ):
                highest_freq_char = curr_char

            if (right_pointer - left_pointer + 1) > (freq_map[highest_freq_char] + k):
                freq_map[s[left_pointer]] -= 1
                left_pointer += 1

        return right_pointer - left_pointer + 1


if __name__ == "__main__":
    s = Solution()
    word = "AABABBA"
    k = 1
    print(s.characterReplacement(word, k))
