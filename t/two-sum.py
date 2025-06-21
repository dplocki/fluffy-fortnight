class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for index, num in enumerate(nums):
            if (target - num) in cache:
                return [cache[target - num], index]
            
            cache[num] = index

        return None
