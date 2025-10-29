class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = list(map(int, s))

        while len(digits) > 2:
            digits = list(map(lambda x: (x[0] + x[1]) % 10, pairwise(digits)))

        return digits[0] == digits[1]
