class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = list()
        
        for index, value in enumerate(nums):
            result.append(nums[(index + value) % n])

        return result
