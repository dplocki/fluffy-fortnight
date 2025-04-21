class Solution:
    def jump(self, nums: List[int]) -> int:
        last_index = len(nums) - 1
        dp = { 0: 0 }
        for index, num in enumerate(nums):
            will_be_jumps = dp.get(index, 0) + 1

            for delta in range(1, num + 1):
                new_index = index + delta
                if new_index <= last_index and (new_index not in dp or will_be_jumps < dp[new_index]):
                    dp[new_index] = will_be_jumps

        return dp[last_index]
