MOD = 10**9 + 7

class Solution:
    def numTilings(self, n: int) -> int:
        self.cache = {}
        return self.find_ways_count(n, 0, False)

    def find_ways_count(self, n: int, index: int, gap: bool) -> int:
        if (index, gap) in self.cache:
            return self.cache[index, gap]

        if index > n:
            self.cache[index, gap] = 0
            return 0

        if index == n:
            self.cache[index, True] = 0
            self.cache[index, False] = 1
            return 0 if gap else 1

        result = 0
        if gap:
            result += self.find_ways_count(n, index + 1, True)
            result += self.find_ways_count(n, index + 1, False)
        else:
            result += self.find_ways_count(n, index + 1, False)
            result += self.find_ways_count(n, index + 2, False)
            result += 2 * self.find_ways_count(n, index + 2, True)

        result %= MOD
        self.cache[index, gap] = result
        return result
