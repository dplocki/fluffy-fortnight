class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = { 0: True }
        options = 0

        for current_index in range(minJump, n):
            if dp.get(current_index - minJump, False):
                options += 1

            if dp.get(current_index - maxJump - 1, False):
                options -= 1

            dp[current_index] = options > 0 and s[current_index] == '0'

        return dp.get(current_index, False)
