class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = { (0, -1): 0 }

        for column_index, value in enumerate(grid[0]):
            dp[0, column_index] = dp[0, column_index - 1] + value

        for row_index, row in enumerate(grid[1:], start=1):
            dp[row_index, 0] = dp[row_index - 1, 0] + row[0]

        for row_index, row in enumerate(grid[1:], start=1):
            for column_index, value in enumerate(row[1:], start=1):
                dp[row_index, column_index] = min(dp[row_index - 1, column_index], dp[row_index, column_index - 1]) + value

        return dp[len(grid) - 1, len(grid[0]) - 1]
