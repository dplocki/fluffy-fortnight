class Solution:
    def reverseDegree(self, s: str) -> int:
        A = ord('a')
        return sum(
            (26 - ord(letter) + A) * (index + 1)
            for index, letter in enumerate(s)
        )
