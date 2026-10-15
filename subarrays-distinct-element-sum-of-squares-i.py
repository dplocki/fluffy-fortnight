class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for start in range(n):
            numbers = set()
            for end in range(start, n):
                numbers.add(nums[end])

                result += len(numbers) ** 2

        return result
