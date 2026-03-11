class Solution:
    def minFlips(self, s: str) -> int:
        target_pattern, n = "01", len(s)
        mismatch_count = sum(char != target_pattern[i & 1] for i, char in enumerate(s))
        result = min(mismatch_count, n - mismatch_count)

        for i in range(n):
            mismatch_count -= s[i] != target_pattern[i & 1]
            mismatch_count += s[i] != target_pattern[(i + n) & 1]

            result = min(result, mismatch_count, n - mismatch_count)
      
        return result
