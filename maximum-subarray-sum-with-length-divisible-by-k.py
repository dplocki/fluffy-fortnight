class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        return max(self.internal(nums, k))

    def internal(self, nums: List[int], k: int) -> Iterable[int]:
        n = len(nums)
        nums_sums = list(accumulate(nums))
        for start in range(0, n - k + 1):
            for multiplayer in count(1):
                s = nums_sums[start - 1] if start > 0 else 0
                end = start + multiplayer * k - 1
                if end >= n:
                    break

                e = nums_sums[end]
                yield e - s
