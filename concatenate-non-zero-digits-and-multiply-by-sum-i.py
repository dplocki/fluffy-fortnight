class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0

        digits = list(map(int, str(n)))
        return int(''.join(map(str, filter(lambda d: d != 0, digits)))) * sum(digits)
