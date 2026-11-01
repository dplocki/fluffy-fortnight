class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        if nums[0] == nums[-1]:
            return 0

        diff = nums[-1] - nums[0]
        return diff + self.minMoves([nums[i] + diff for i in range(len(nums) - 1)] + [nums[-1]])
