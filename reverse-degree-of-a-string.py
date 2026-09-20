class Solution:
    def reverseDegree(self, s: str) -> int:
        prefix = ord('a') + 26
        return sum(
            (prefix - ord(letter)) * (index + 1)
            for index, letter in enumerate(s)
        )
