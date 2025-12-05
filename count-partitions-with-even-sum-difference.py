class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        p = list(accumulate(nums))

        return sum(1
            for i in range(1, n)
            if (p[i - 1] - (p[-1] - p[i - 1])) % 2 == 0)
