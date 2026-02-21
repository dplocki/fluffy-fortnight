class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19])

        return sum(1
            for n in range(left, right + 1)
            if self.countSetBits(n) in primes)

    def countSetBits(self, n: int) -> int:
        count = 0
        while (n):
            count += n & 1
            n >>= 1

        return count
