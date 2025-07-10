class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) >> 1

            if nums[middle] > nums[right]:
                if nums[left] <= target <= nums[middle]:
                    right = middle
                else:
                    left = middle + 1
            elif nums[middle] < nums[right]:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle
            else:
                right -= 1

        return nums[left] == target
