class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = { (-1, 0): 0, (-1, 1): 0, (-1, 2): 0 }

        for index, num in enumerate(nums):
            dp[index, 0] = dp[index - 1, 0]
            dp[index, 1] = dp[index - 1, 1]
            dp[index, 2] = dp[index - 1, 2]

            x = dp[index - 1, 0] + num
            dp[index, x % 3] = max(x, dp.get((index, x % 3), 0))

            x = dp[index - 1, 1] + num
            dp[index, x % 3] = max(x, dp.get((index, x % 3), 0))

            x = dp[index - 1, 2] + num
            dp[index, x % 3] = max(x, dp.get((index, x % 3), 0))

        return dp[index, 0]
