class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = {}
        result = 0

        for row_index, row in enumerate(matrix):
            for column_index, cell in enumerate(row):
                if cell == 0:
                    dp[row_index, column_index] = 0
                    continue

                max_squre = 1 + min(
                    dp.get((row_index - 1, column_index), 0),
                    dp.get((row_index, column_index - 1), 0),
                    dp.get((row_index - 1, column_index - 1), 0))

                dp[row_index, column_index] = max_squre
                result += max_squre

        return result
