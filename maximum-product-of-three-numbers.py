class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        return max(
            reduce(operator.mul, numbers, 1)
            for numbers in combinations(nums, 3)
        )
