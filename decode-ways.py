class Solution:
    def numDecodings(self, s: str) -> int:
        valid_tokens = { str(index + 1) for index, _ in enumerate(string.ascii_lowercase) }
        dp = { -1: 1 }

        prev = ' '
        for index, character in enumerate(s):
            dp[index] = dp.get(index - 1, 0) if character in valid_tokens else 0
            if prev + character in valid_tokens:
                dp[index] += dp.get(index - 2, 0)
            
            prev = character

        return dp[len(s) - 1]
