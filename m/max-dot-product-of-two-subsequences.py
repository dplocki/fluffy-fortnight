class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        dp = {}
        for i1 in range(n1):
            for i2 in range(n2):
                dp[i1 + 1, i2 + 1] = max(
                    dp.get((i1, i2 + 1), float('-inf')),
                    dp.get((i1 + 1, i2), float('-inf')),
                    max(0, dp.get((i1, i2), float('-inf'))) + nums1[i1] * nums2[i2]
                )

        return dp[n1, n2]
