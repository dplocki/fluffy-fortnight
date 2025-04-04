class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0    

        left = 0
        right = len(nums) - 1

        while right >= 0:
            if nums[right] == val:
                right -= 1
            else:
                if nums[left] == val:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
                else:
                    left += 1

                if left < right:
                    continue 

                return right + 1

        return 0
