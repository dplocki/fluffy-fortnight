class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        result = 0

        for start, letter in enumerate(s):
            letters = {}

            for end in range(start, n):
                letters[s[end]] = letters.get(s[end], 0) + 1
                if len(set(letters.values())) == 1:
                    result = max(result, end - start + 1)

        return result
