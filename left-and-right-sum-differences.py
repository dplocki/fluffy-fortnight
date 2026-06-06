class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = []
        current = 0
        for num in nums:
            left_sum.append(current)
            current += num

        right_sum = []
        current = 0
        for num in reversed(nums):
            right_sum.append(current)
            current += num
        
        return [abs(l - r) for l, r in zip(left_sum, reversed(right_sum))]
