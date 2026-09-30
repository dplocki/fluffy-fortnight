class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [1]
        last = {}

        for index, letter in enumerate(s):
            dp.append(dp[-1] * 2)
            if letter in last:
                dp[-1] -= dp[last[letter]]

            last[letter] = index

        return (dp[-1] - 1) % (10**9 + 7)
