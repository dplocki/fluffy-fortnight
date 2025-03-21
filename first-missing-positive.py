class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maximum = len(nums)
        excludes = maximum * [False]

        for num in nums:
            if 0 < num <= maximum:
                excludes[num - 1] = True

        for index, exclude in enumerate(excludes):
            if not exclude:
                return index + 1

        return maximum + 1
