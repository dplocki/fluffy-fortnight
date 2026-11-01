class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        result = -1

        for num, correct_num in zip(nums, range(len(nums))):
            if num == correct_num:
                continue

            result &= num

        if result == -1:
            return 0

        return result
