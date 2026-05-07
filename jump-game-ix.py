class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        
        maxium_jump = nums[0]
        for num in nums[1:]:
            maxium_jump = max(maxium_jump, num)
            result.append(maxium_jump)

        maxium_jump_index = len(nums) - 1
        for index in range(len(nums) - 2, -1, -1):
            if result[index] > nums[maxium_jump_index]:
                result[index] = result[maxium_jump_index]

            if nums[index] < nums[maxium_jump_index]:
                maxium_jump_index = index

        return result
