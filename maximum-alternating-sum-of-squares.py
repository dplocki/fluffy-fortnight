class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums_sqrs = list(map(lambda n: n**2, nums))
        nums_sqrs.sort()
        termitus = ceil(len(nums) / 2)
        return sum(nums_sqrs[-termitus:]) - sum(nums_sqrs[:-termitus])
