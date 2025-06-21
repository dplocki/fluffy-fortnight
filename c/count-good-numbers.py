class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even_indexes = (n + 1) // 2
        odd_indexes = n // 2

        return pow(5, even_indexes, mod) * pow(4, odd_indexes, mod) % mod
