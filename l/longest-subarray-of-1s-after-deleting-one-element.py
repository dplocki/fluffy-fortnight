class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums_length = len(nums)
        lefts = { 0: 0 }
        rights = { nums_length: 0 }

        for index, n in enumerate(nums, 1):
            lefts[index] = lefts[index - 1] + 1 if n == 1 else 0

        for index in range(nums_length - 1, -1, -1):
            rights[index] = rights[index + 1] + 1 if nums[index] == 1 else 0

        return max(lefts[index] + rights[index + 1] for index in range(nums_length))
