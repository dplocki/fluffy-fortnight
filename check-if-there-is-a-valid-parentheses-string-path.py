class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows, columns = len(grid), len(grid[0])
        
        if grid[0][0] != "(" or grid[rows - 1][columns - 1] != ")":
            return False

        dp = defaultdict(int)
        dp[0, 0] = 2

        for r in range(rows):
            for c in range(columns):
                if r > 0:
                    if grid[r][c] == '(':
                        dp[r, c] |= dp[r - 1, c] << 1
                    else:
                        dp[r, c] |= dp[r - 1, c] >> 1

                if c > 0:
                    if grid[r][c] == '(':
                        dp[r, c] |= dp[r, c - 1] << 1
                    else:
                        dp[r, c] |= dp[r, c - 1] >> 1
        
        return bool(dp[rows - 1, columns - 1] & 1)
