class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        return max(self.internal(nums, k))

    def internal(self, nums: List[int], k: int) -> Iterable[int]:
        min_prefix_sum = [float(inf)] * (k - 1) + [0]
        accumulate_sum = 0

        for index, value in enumerate(nums):
            accumulate_sum += value
            remainder = index % k
            yield accumulate_sum - min_prefix_sum[remainder]
            min_prefix_sum[remainder] = min(min_prefix_sum[remainder], accumulate_sum)
