class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_length = len(word1)
        word2_length = len(word2)
        dp = defaultdict(int)

        for index in range(1, word2_length + 1):
            dp[0, index] = index

        for index_1 in range(1, word1_length + 1):
            dp[index_1, 0] = index_1

            for index_2 in range(1, word2_length + 1):
                if word1[index_1 - 1] == word2[index_2 - 1]:
                    dp[index_1, index_2] = dp[index_1 - 1, index_2 - 1]
                else:
                    dp[index_1, index_2] = min(
                        dp[index_1 - 1, index_2],
                        dp[index_1, index_2 - 1],
                        dp[index_1 - 1, index_2 - 1]
                    ) + 1
        
        return dp[word1_length, word2_length]
