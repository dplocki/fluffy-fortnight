class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries)

        while left < right:
            mid = (left + right + 1) >> 1

            gain_power = sum(min(bettery, mid) for bettery in batteries)

            if gain_power >= n * mid:
                left = mid
            else:
                right = mid - 1

        return left
