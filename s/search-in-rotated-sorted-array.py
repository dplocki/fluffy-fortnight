class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[0] <= nums[middle]:
                if nums[0] <= target <= nums[middle]:
                    right = middle
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[-1]:
                    left = middle + 1
                else:
                    right = middle

        return left if nums[left] == target else -1
