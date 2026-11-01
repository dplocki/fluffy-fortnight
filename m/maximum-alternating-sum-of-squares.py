class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums_sqrs = list(map(lambda n: n**2, nums))
        nums_sqrs.sort()
        n = len(nums)
        return sum(nums_sqrs[n >> 1:]) - sum(nums_sqrs[:n >> 1])
