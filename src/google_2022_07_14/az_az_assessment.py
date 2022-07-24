import heapq
import random
from collections import Counter
from itertools import permutations

class Result1:
    _vowels: set[str] = {'a', 'e', 'i', 'o', 'u'}

    @staticmethod
    def findPasswordStrength(password: str) -> int:
        strength = 0
        has_vowel = False
        has_cons = False

        for c in password:
            if has_cons and has_vowel:
                strength += 1
                has_cons = False
                has_vowel = False
            if c in Result1._vowels:
                has_vowel = True
            else:
                has_cons = True

        return strength


class Result2:
    @staticmethod
    def backtrack_combos(popularity: list[int], idx: int, combo: int, combos: list[int], k: int) -> None:
        if idx > len(popularity):
            return
        heapq.heappush(combos, combo)
        for i in range(idx, len(popularity)):
            Result2.backtrack_combos(popularity, i + 1, combo + popularity[i], combos, k)
            while len(combos) > k:
                heapq.heappop(combos)

    @staticmethod
    def bestCombo(popularity: list[int], k: int) -> list[int]:
        combos = []
        Result2.backtrack_combos(popularity, 0, 0, combos, k)

        return heapq.nlargest(k, combos)

if __name__ == "__main__":
    # print(Result1.findPasswordStrength("hackerrank"))
    # print(Result1.findPasswordStrength(""))
    # print(Result1.findPasswordStrength("aaaaaa"))
    # print(Result1.findPasswordStrength(""))
    # print(Result2.bestCombo([3, 5, -2], 3))
    # print(Result2.bestCombo([1, 2, 3, 1000], 4))
    # print(Result2.bestCombo([0, 0, 0, 0, 0], 3))
    # print(Result2.bestCombo([-10, -5, -3, -2, -1, 0, 5], 20))
    random.seed(7)
    popularity = []
    for _ in range(25):
        popularity.append(random.randint(-10, 10))
    print(Result2.bestCombo(popularity, 10))