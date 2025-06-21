class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect.bisect_left(nums, target)
        if start >= len(nums) or nums[start] != target:
            return [-1, -1]

        last = bisect.bisect_right(nums, target) - 1
        return [start, last]
