class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        return sum(k for k, v in Counter(nums).items() if v == 1)
