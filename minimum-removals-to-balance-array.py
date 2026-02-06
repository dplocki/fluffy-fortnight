class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, result = 0, n

        for right, value in enumerate(nums):
            while left < right and nums[left] * k < value:
                left += 1

            result = min(result, n - right + left - 1)

        return result
