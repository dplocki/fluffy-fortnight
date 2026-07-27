class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        reach, far = [0] * n, 0

        for i in range(n):
            if i == 0 or nums[i] - nums[i-1] > maxDiff:
                far = i

            reach[i] = far

        return [
            reach[max(start, end)] <= reach[min(start, end)]
            for start, end in queries
        ]
