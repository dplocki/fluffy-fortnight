class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(map(lambda a: abs(a[0] - a[1]), zip(nums, nums[1:])), default=0)
