class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        pivot = -1
        for index in range(nums_len - 2, -1, -1):
            if nums[index] < nums[index + 1]:
                pivot = index
                break

        if pivot == -1:
            nums.reverse()
            return

        for index in range(nums_len - 1, pivot, -1):
            if nums[index] > nums[pivot]:
                nums[index], nums[pivot] = nums[pivot], nums[index]
                break

        left, right = pivot + 1, nums_len - 1    
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
