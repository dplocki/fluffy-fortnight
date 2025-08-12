class Solution:
    def minCut(self, s: str) -> int:
        s_length = len(s)
        is_palindrom = self.build_is_palindrom(s_length, s)
        dp = list(range(s_length))

        for end in range(1, s_length):
            for start in range(end + 1):
                if not is_palindrom[start, end]:
                    continue

                dp[end] = min(dp[end], 0 if start == 0 else 1 + dp[start - 1])

        return dp[-1]

    def build_is_palindrom(self, s_length: int, s: str):
        result = { (i, i):True for i in range(s_length) }

        for start in reversed(range(s_length)):
            for end in range(start + 1, s_length):
                result[start, end] = s[start] == s[end] and result.get((start + 1, end - 1), True)

        return result
