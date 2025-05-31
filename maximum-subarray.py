class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = 0
        current_sum = 0

        for num in nums:
            current_sum = max(num + current_sum, num)
            result = max(current_sum, result)
        
        return result
