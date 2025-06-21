class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        move_index = 1

        for current in range(1, len(nums)):
            if nums[current] != nums[current - 1]:
                nums[move_index] = nums[current]
                move_index += 1

        return move_index
