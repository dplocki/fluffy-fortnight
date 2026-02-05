class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        return nums[0] + sum(sorted(sorted(nums[1:])[:2]))
