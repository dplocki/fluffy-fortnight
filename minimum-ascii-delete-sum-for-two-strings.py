class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1_len, s2_len = len(s1), len(s2)
        dp = { (0, 0): 0 }

        for index1 in range(1, s1_len + 1):
            dp[index1, 0] = ord(s1[index1 - 1]) + dp[index1 - 1, 0]

        for index2 in range(1, s2_len + 1):
            dp[0, index2] = ord(s2[index2 - 1]) + dp[0, index2 - 1]

        for index1 in range(1, s1_len + 1):
            letter1 = ord(s1[index1 - 1]) if index1 > 0 else 0

            for index2 in range(1, s2_len + 1):
                letter2 = ord(s2[index2 - 1]) if index2 > 0 else 0

                dp[index1, index2] = min(
                    dp.get((index1 - 1, index2 - 1), 0) + (letter1 + letter2 if letter1 != letter2 else 0),
                    dp.get((index1, index2 - 1), 0) + letter2,
                    dp.get((index1 - 1, index2), 0) + letter1,
                )

        return dp[s1_len, s2_len]
