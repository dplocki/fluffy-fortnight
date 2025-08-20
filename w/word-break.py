class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = { 0: True }

        for end in range(1, len(s) + 1):
            for start in range(end):
                if not dp.get(start, False):
                    continue

                if s[start:end] in words:
                    dp[end] = True
                    break

        return dp.get(len(s), False)
