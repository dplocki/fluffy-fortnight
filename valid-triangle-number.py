class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        return sum(1
            for a, b, c in combinations(nums, 3)
            if a < b + c and b < a + c and c < a + b)
