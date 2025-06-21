class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxium_reach = 0

        for index, num in enumerate(nums):
            if index > maxium_reach:
                return False
            
            maxium_reach = max(maxium_reach, index + num)

        return True
