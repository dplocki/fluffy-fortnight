class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n == 0:
            return False

        sorted_nums = sorted(nums)

        if any(a != b for a, b in zip(range(1, n + 1), sorted_nums)):
            return False
        
        return sorted_nums[-2] == sorted_nums[-1] == n
