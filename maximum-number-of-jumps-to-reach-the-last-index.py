class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = { 0: 0 }

        for i in range(n - 1):
            for j in range(i + 1, n):
                if i not in dp:
                    continue

                if abs(nums[j] - nums[i]) > target:
                    continue

                dp[j] = max(dp.get(j, -1), dp[i] + 1)

        return dp.get(n - 1, -1)
