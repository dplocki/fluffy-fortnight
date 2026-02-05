class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = nums[:]
        
        for index, value in enumerate(nums):
            result[index] = nums[(index + value) % n]

        return result
