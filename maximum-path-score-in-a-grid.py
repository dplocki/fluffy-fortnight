class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        dp = {}
        for i in range(k + 1):
            dp[-1, 0, i] = 0
            dp[0, -1, i] = 0

        m = 0
        for row_index, row in enumerate(grid):
            m += 1

            n = 0
            for column_index, value in enumerate(row):
                n += 1

                if value == 0:
                    for i in range(k + 1):
                        dp[row_index, column_index, i] = max(dp.get((row_index - 1, column_index, i), -1), dp.get((row_index, column_index - 1, i), -1))
                else:
                    for i in range(1, k + 1):
                        top = dp.get((row_index - 1, column_index, i - 1), -1)
                        top = -1 if top == -1 else top + value

                        left = dp.get((row_index, column_index - 1, i - 1), -1)
                        left = -1 if left == -1 else left + value

                        dp[row_index, column_index, i] = max(top, left)

        return max(dp.get((m - 1, n - 1, i), -1) for i in range(k + 1))
