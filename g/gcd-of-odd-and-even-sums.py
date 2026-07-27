class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # sum of all odd numbers before n is: n*n
        # sum of all even numbers before n is: n*(n + 1)
        # GCD(n*n, n*(n + 1))
        return n
