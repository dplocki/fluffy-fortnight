class Solution:
    MODULO = 10**9 + 7

    def concatenatedBinary(self, n: int) -> int:
        result = 0
        digits_number = 1
        number_limit = 2

        for i in range(n + 1):
            if i == number_limit:
                digits_number += 1
                number_limit <<= 1

            result = ((result << digits_number) | i) % Solution.MODULO

        return result
