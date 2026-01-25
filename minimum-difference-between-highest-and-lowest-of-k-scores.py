class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        return min(
            nums[i + k - 1] - nums[i]
            for i in range(n - k + 1)
        )
