class Solution:

    @lru_cache(maxsize=None)
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        return sum(
            self.numTrees(left) * self.numTrees(n - left - 1)
            for left in range(0, n))
