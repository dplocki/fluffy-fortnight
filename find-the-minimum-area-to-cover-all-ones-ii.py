class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rows_count = len(grid)
        columns_count = len(grid[0])

        def minimum_area(top_row: int, bottom_row: int, left_column: int, right_column: int):
            lc = tr = inf
            rc = br = -inf

            for r in range(top_row, bottom_row + 1):
                for c in range(left_column, right_column + 1):
                    if grid[r][c] == 1:
                        lc = min(lc, c)
                        tr = min(tr, r)
                        rc = max(rc, c)
                        br = max(br, r)

            return (br - tr + 1) * (rc - lc + 1)

        result = rows_count * columns_count

        for r1 in range(0, rows_count - 1):
            for r2 in range(0, rows_count -1):
                result = min(result,
                    minimum_area(0, r1, 0, columns_count - 1)
                    + minimum_area(r1 + 1, r2, 0, columns_count - 1)
                    + minimum_area(r2 + 1, rows_count - 1, 0, columns_count - 1))

        for c1 in range(0, columns_count - 1):
            for c2 in range(0, columns_count -1):
                result = min(result,
                    minimum_area(0, rows_count - 1, 0, c1)
                    + minimum_area(0, rows_count - 1, c1 + 1, c2)
                    + minimum_area(0, rows_count - 1, c2 + 1, columns_count - 1))

        for r in range(rows_count - 1):
            for c in range(columns_count - 1):
                result = min(result,
                    minimum_area(0, r, 0, c)
                    + minimum_area(0, r, c + 1, columns_count - 1)
                    + minimum_area(r + 1, rows_count - 1, 0, columns_count - 1))
                
                result = min(result,
                    minimum_area(0, r, 0, c)
                    + minimum_area(r + 1, rows_count - 1, 0, c)
                    + minimum_area(0, rows_count - 1, c + 1, columns_count - 1))
                
                result = min(result,
                    minimum_area(0, rows_count - 1, 0, c)
                    + minimum_area(0, r, c + 1, columns_count - 1)
                    + minimum_area(r + 1, rows_count - 1, c + 1, columns_count - 1))
                
                result = min(result,
                    minimum_area(0, r, 0, columns_count - 1)
                    + minimum_area(r + 1, rows_count - 1, 0, c)
                    + minimum_area(r + 1, rows_count - 1, c + 1, columns_count - 1))

        return result
