class Solution:
    def isMatch(self, sequence: str, pattern: str) -> bool:
        sequence_size = len(sequence) + 1
        pattern_size = len(pattern) + 1

        dp = defaultdict(bool)
        dp[0, 0] = True

        for pattern_index in range(1, pattern_size):
            if pattern[pattern_index - 1] == '*':
                dp[0, pattern_index] = dp[0, pattern_index - 1]

        for sequence_index in range(1, sequence_size):
            for pattern_index in range(1, pattern_size):
                if sequence[sequence_index - 1] == pattern[pattern_index - 1] or pattern[pattern_index - 1] == '?':
                    dp[sequence_index, pattern_index] = dp[sequence_index - 1, pattern_index - 1]
                elif pattern[pattern_index - 1] == '*':
                    dp[sequence_index, pattern_index] = dp[sequence_index - 1, pattern_index] or dp[sequence_index, pattern_index - 1]

        return dp[sequence_size - 1, pattern_size - 1]
