class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0

        for right, value in enumerate(nums):
            if nums[right] > nums[left] * k:
                left += 1

        return left
