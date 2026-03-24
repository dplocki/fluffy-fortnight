class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])
        result = []

        for r in range(rows - k + 1):
            row = []

            for c in range(columns - k + 1):
                submatrix = set(
                    grid[r + rk][c + ck]
                    for ck in range(k)
                    for rk in range(k)
                )

                row.append(0 if len(submatrix) == 1 else min(
                    map(lambda e: abs(e[0] - e[1]), combinations(submatrix, 2))
                ))

            result.append(row)
        
        return result
