class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n, total = len(nums), sum(nums)

        result = f = sum(index * num for index, num in enumerate(nums))
        for current in range(1, n):
            f = f + total - n * nums[n - current]
            result = max(result, f)

        return result
