class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result = 1
        increasing, decreasing = 1, 1

        for index in range(1, len(nums)):
            if nums[index - 1] < nums[index]:
                increasing += 1
                decreasing = 1
            else:
                increasing = 1

            if nums[index - 1] > nums[index]:
                decreasing += 1
            else:
                decreasing = 1
                
            result = max(result, increasing, decreasing)

        return result
