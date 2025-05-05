MOD = 10**9 + 7

class Solution:
    def numTilings(self, n: int) -> int:
        return self.find_ways_count(n, 0, False)

    def find_ways_count(self, n: int, index: int, gap: bool) -> int:
        if index > n:
            return 0

        if index == n:
            return 0 if gap else 1

        result = 0
        if gap:
            result += self.find_ways_count(n, index + 1, True)
            result += self.find_ways_count(n, index + 1, False)
        else:
            result += self.find_ways_count(n, index + 1, False)
            result += self.find_ways_count(n, index + 2, False)
            result += 2 * self.find_ways_count(n, index + 2, True)

        return result % MOD
