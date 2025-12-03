class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]

        for num in nums:
            for d in dp[:]:
                x = d + num
                dp[x % 3] = max(x, dp[x % 3])

        return dp[0]
