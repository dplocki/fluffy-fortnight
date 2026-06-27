class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        the_longest_strick = 0
        dp = {}

        for num in sorted(counter, reverse=True):
            if counter[num] > 1:
                dp[num] = dp.get(num ** 2, 0) + 1
            else:
                dp[num] = 1

            the_longest_strick = max(the_longest_strick, dp[num])

        return max(
            ((the_longest_strick - 1) << 1) + 1,
            (counter[1] - 1) if counter[1] % 2 == 0 else counter[1]
        )
