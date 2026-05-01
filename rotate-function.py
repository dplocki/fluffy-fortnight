class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        result = [0] * n

        for current in range(n):
            for start_index in range(n):
                result[start_index] += current * nums[(start_index + current) % n]

        return max(result)
