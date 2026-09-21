class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k

        dp = [0] * k
        for num in nums:
            new_dp = [0] * k
            new_dp[num % k] += 1

            for r in range(k):
                new_dp[(num * r) % k] += dp[r]

            dp = new_dp

            for i in range(k):
                result[i] += dp[i]
           
        return result
