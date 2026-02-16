class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        multiplayer = 2**31
        while n != 0:
            result += multiplayer * (n & 1)
            multiplayer >>= 1
            n >>= 1

        return result
