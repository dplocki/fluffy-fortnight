class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, middle, right = 0, 0, len(nums) - 1

        while middle <= right:
            if nums[middle] == 0:
                nums[left], nums[middle] = nums[middle], nums[left]
                left += 1
                middle += 1
            elif nums[middle] == 2:
                nums[right], nums[middle] = nums[middle], nums[right]
                right -= 1
            else:
                middle += 1

        return nums
