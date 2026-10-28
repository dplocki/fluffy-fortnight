class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        dp = [set() for _ in range(columns)]
        dp[0].add(grid[0][0])

        for r in range(rows):
            for c in range(columns):
                if r == 0 and c == 0:
                    continue

                value = grid[r][c]
                dp[c] = {k ^ value
                    for k in (dp[c] | (dp[c - 1] if c > 0 else set()))
                }

        return min(dp[-1])
