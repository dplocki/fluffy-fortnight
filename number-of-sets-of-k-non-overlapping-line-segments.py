MOD = 10**9 + 7


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, k * 2) % MOD
