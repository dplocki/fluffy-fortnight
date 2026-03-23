class Solution:
    MOD = 10 ** 9 + 7

    def maxProductPath(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        dp_mins = { (0, 0): grid[0][0] }
        dp_maxs = { (0, 0): grid[0][0] }

        for r in range(1, rows):
            dp_mins[r, 0] = dp_mins[r - 1, 0] * grid[r][0]
            dp_maxs[r, 0] = dp_maxs[r - 1, 0] * grid[r][0]

        for c in range(1, columns):
            dp_mins[0, c] = dp_mins[0, c - 1] * grid[0][c]
            dp_maxs[0, c] = dp_maxs[0, c - 1] * grid[0][c]

        for r in range(1, rows):
            for c in range(1, columns):
                value = grid[r][c]
                if value >= 0:
                    dp_mins[r, c] = value * min(dp_mins.get((r - 1, c), 1), dp_mins.get((r, c - 1), 1))
                    dp_maxs[r, c] = value * max(dp_maxs.get((r - 1, c), 1), dp_maxs.get((r, c - 1), 1))
                else:
                    dp_mins[r, c] = value * max(dp_maxs.get((r - 1, c), 1), dp_maxs.get((r, c - 1), 1))
                    dp_maxs[r, c] = value * min(dp_mins.get((r - 1, c), 1), dp_mins.get((r, c - 1), 1))

        result = dp_maxs[len(grid)-1, len(grid[0])-1]
        return -1 if result < 0 else result % Solution.MOD
