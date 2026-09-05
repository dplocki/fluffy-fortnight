class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maximums = accumulate(nums, max)
        minimums = reversed(list(accumulate(reversed(nums), min)))
        indexes = (x - n for x, n in zip(maximums, minimums))

        return min((index for index, score in enumerate(indexes) if score <= k), default=-1)
