class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len + s2_len != len(s3):
            return False

        dp = [False] * (s2_len + 1)
        dp[0] = True

        for s2_index in range(1, s2_len + 1):
            dp[s2_index] = dp[s2_index - 1] and s2[s2_index - 1] == s3[s2_index - 1]

        for s1_index in range(1, s1_len + 1):
            dp[0] = dp[0] and s1[s1_index - 1] == s3[s1_index - 1]
            for s2_index in range(1, s2_len + 1):
                dp[s2_index] = (dp[s2_index] and s1[s1_index - 1] == s3[s1_index + s2_index - 1]) or \
                    (dp[s2_index - 1] and s2[s2_index - 1] == s3[s1_index + s2_index - 1])

        return dp[s2_len]
