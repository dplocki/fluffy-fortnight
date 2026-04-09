class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        rows, columns = len(coins), len(coins[0])
        dp = {
            (-1, 0, 2): 0, (0, -1, 2): 0,
            (-1, 0, 1): -inf, (0, -1, 1): -inf,
            (-1, 0, 0): -inf, (0, -1, 0): -inf,
        }
    
        for c in range(columns):
            value = coins[0][c]
            if value >= 0:
                dp[0, c, 2] = dp[0, c - 1, 2] + value
                dp[0, c, 1] = dp[0, c - 1, 1] + value
                dp[0, c, 0] = dp[0, c - 1, 0] + value
            else:
                dp[0, c, 2] = dp[0, c - 1, 2] + value
                dp[0, c, 1] = max(dp[0, c - 1, 2], dp[0, c - 1, 1] + value)
                dp[0, c, 0] = max(dp[0, c - 1, 1], dp[0, c - 1, 0] + value)

        for r in range(rows):
            value = coins[r][0]
            if value >= 0:
                dp[r, 0, 2] = dp[r - 1, 0, 2] + value
                dp[r, 0, 1] = dp[r - 1, 0, 1] + value
                dp[r, 0, 0] = dp[r - 1, 0, 0] + value
            else:
                dp[r, 0, 2] = dp[r - 1, 0, 2] + value
                dp[r, 0, 1] = max(dp[r - 1, 0, 2], dp[r - 1, 0, 1] + value)
                dp[r, 0, 0] = max(dp[r - 1, 0, 1], dp[r - 1, 0, 0] + value)

        for r in range(1, rows):
            for c in range(1, columns):
                value = coins[r][c]
                if value >= 0:
                    dp[r, c, 2] = max(dp[r - 1, c, 2], dp[r, c - 1, 2]) + value
                    dp[r, c, 1] = max(dp[r - 1, c, 1], dp[r, c - 1, 1]) + value
                    dp[r, c, 0] = max(dp[r - 1, c, 0], dp[r, c - 1, 0]) + value
                else:
                    dp[r, c, 2] = max(dp[r - 1, c, 2], dp[r, c - 1, 2])
                    dp[r, c, 1] = max(dp[r - 1, c, 1], dp[r, c - 1, 1])
                    dp[r, c, 0] = max(dp[r - 1, c, 0], dp[r, c - 1, 0])

                    dp[r, c, 0] = max(dp[r, c, 1], dp[r, c, 0] + value)
                    dp[r, c, 1] = max(dp[r, c, 2], dp[r, c, 1] + value)
                    dp[r, c, 2] += value

        return max(dp[r, c, 0], dp[r, c, 1], dp[r, c, 2])
