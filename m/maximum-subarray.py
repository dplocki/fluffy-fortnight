class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        iter_nums = iter(nums)
        result = current_sum = next(iter_nums)

        for num in iter_nums:
            current_sum = max(num + current_sum, num)
            result = max(current_sum, result)
        
        return result
