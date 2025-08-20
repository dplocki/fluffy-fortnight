class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maximum = max(nums)
        if maximum < 0:
            return maximum

        return sum(filter(lambda n: n > 0, set(nums)))
