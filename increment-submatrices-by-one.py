class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]

        for row1, col1, row2, col2 in queries:
            result[row1][col1] += 1

            if col2 + 1 < n:
                result[row1][col2 + 1] -= 1

            if row2 + 1 < n:
                result[row2 + 1][col1] -= 1

            if col2 + 1 < n and row2 + 1 < n:
                result[row2 + 1][col2 + 1] += 1

        for r in range(n):
            for c in range(n):
                if r > 0:
                    result[r][c] += result[r - 1][c]

                if c > 0:
                    result[r][c] += result[r][c - 1]

                if r > 0 and c > 0:
                    result[r][c] -= result[r - 1][c - 1]

        return result
