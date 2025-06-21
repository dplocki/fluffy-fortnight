class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        result = 0

        for k in range(0, len(nums) + 1):
            if k < len(nums) and nums[k] <= k:
                continue
            
            if k > 0 and nums[k - 1] >= k:
                continue

            result += 1

        return result
