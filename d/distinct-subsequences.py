class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        t_length = len(t)
        dp = defaultdict(int)
        dp[0] = 1

        for character in s:
            for t_index in range(t_length, 0, -1):
                if character == t[t_index - 1]:
                    dp[t_index] += dp[t_index - 1]

        return dp[t_length]
