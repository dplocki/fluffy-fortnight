class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        total_xor = 0
        all_zero = True

        for x in nums:
            total_xor ^= x
            if x > 0:
                all_zero = False

        if total_xor > 0:
            return n

        return n - 1 if all_zero == False else 0
