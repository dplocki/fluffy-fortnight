class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = defaultdict(int)

        for transactions in range(1, k + 1):
            dp[0, transactions, 1] = -prices[0]
            dp[0, transactions, 2] = prices[0]

        for day in range(1, n):
            for transactions in range(1, k + 1):
                dp[day, transactions, 0] = max(
                    dp[day - 1, transactions, 0],
                    dp[day - 1, transactions, 1] + prices[day],
                    dp[day - 1, transactions, 2] - prices[day]
                )

                dp[day, transactions, 1] = max(
                    dp[day - 1, transactions, 1],
                    dp[day - 1, transactions - 1, 0] - prices[day]
                )

                dp[day, transactions, 2] = max(
                    dp[day - 1, transactions, 2],
                    dp[day - 1, transactions - 1, 0] + prices[day]
                )

        return dp[n - 1, k, 0]
