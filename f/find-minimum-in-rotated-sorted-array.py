class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        middle = 0

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            if left + 1 == right:
                return nums[right]

            middle = left + ((right - left) >> 1)
            if nums[left] > nums[middle]:
                right = middle
            else:
                left = middle
        
        return nums[middle]
