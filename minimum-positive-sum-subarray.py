class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n, result = len(nums), inf

        for start in range(n):
            current_sum = 0

            for end in range(start, min(start + r, n)):
                current_sum += nums[end]
                if end - start + 1 >= l and 0 < current_sum < result:
                    result = current_sum

        return -1 if result == inf else result
