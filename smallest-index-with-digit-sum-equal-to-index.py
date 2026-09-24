class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        return next(
            (index for index, num in enumerate(nums) if sum(map(int, str(num))) == index),
            -1
        )
