class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = { -1: 0, -2: 0 }

        for index, n in enumerate(nums):
            dp[index] = max(dp[index - 1], dp[index - 2] + n)

        return dp[len(nums) - 1]
