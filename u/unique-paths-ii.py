class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = defaultdict(int)
        dp[-1, 0] = 1
       
        for row_index, row in enumerate(obstacleGrid):
            for column_index, obstacle in enumerate(row):
                dp[row_index, column_index] = 0 if obstacle == 1 \
                    else dp[row_index - 1, column_index] + dp[row_index, column_index - 1]

        return dp[len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1]
