class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = left_sum = [0] + list(accumulate(nums[:-1]))
        right_sum = [0] + list(accumulate(reversed(nums)))[:-1]
        
        return [abs(l - r) for l, r in zip(left_sum, reversed(right_sum))]
