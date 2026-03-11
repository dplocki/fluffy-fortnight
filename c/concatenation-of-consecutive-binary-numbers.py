class Solution:
    MODULO = 10**9 + 7

    def concatenatedBinary(self, n: int) -> int:
        result = 0
        for i in range(n + 1):
            result = ((result << i.bit_length()) | i) % Solution.MODULO

        return result
