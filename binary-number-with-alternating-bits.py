class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = None

        while n != 0:
            bit = n % 2
            if bit == prev:
                return False

            prev = bit
            n >>= 1

        return True
