class Solution:
    MOD = 10**9 + 7

    def countPartitions(self, nums: List[int], k: int) -> int:
        sorted_window = SortedList()
        n = len(nums)
        result = None
        dp = { 0: 1 }
        left = 1

        for right in range(1, n + 1):
            sorted_window.add(nums[right - 1])

            while sorted_window[-1] - sorted_window[0] > k:
                sorted_window.remove(nums[left - 1])
                left += 1

            result = dp[right - 1]
            if left >= 2:
                result -= dp[left - 2]

            dp[right] = dp[right - 1] + result

        return result % Solution.MOD
