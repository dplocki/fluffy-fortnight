class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = defaultdict(int)
        dp[0] = 0

        iterator = iter(enumerate(s))
        next(iterator, None)

        for index, character in iterator:
            if character == '(':
                continue

            if s[index - 1] == '(':
                dp[index] = dp[index - 2] + 2
            else:
                potentail_close_index = index - dp[index - 1] - 1
                if potentail_close_index >= 0 and s[potentail_close_index] == '(':
                    dp[index] = dp[index - 1] + 2 + dp[potentail_close_index - 1]

        return max(dp.values())
