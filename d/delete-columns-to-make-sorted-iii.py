class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns_count = len(strs[0])
        dp = [1] * columns_count

        for current_column in range(columns_count):
            for prev_column in range(current_column):
                if all(string[prev_column] <= string[current_column] for string in strs):
                    dp[current_column] = max(dp[current_column], dp[prev_column] + 1)

        return columns_count - max(dp)
