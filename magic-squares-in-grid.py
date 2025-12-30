class Solution:
    MAGIC_DIGITS = set(range(1, 10))

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0

        return sum(1
            for row_index in range(n - 2)
            for column_index in range(m - 2)
            if (grid[row_index][column_index] + grid[row_index + 1][column_index] + grid[row_index + 2][column_index]
                == grid[row_index][column_index + 1] + grid[row_index + 1][column_index + 1] + grid[row_index + 2][column_index + 1]
                == grid[row_index][column_index + 2] + grid[row_index + 1][column_index + 2] + grid[row_index + 2][column_index + 2]

                == grid[row_index][column_index] + grid[row_index][column_index + 1] + grid[row_index][column_index + 2]
                == grid[row_index + 1][column_index] + grid[row_index + 1][column_index + 1] + grid[row_index + 1][column_index + 2]
                == grid[row_index + 2][column_index] + grid[row_index + 2][column_index + 1] + grid[row_index + 2][column_index + 2]

                == grid[row_index][column_index] + grid[row_index + 1][column_index + 1] + grid[row_index + 2][column_index + 2]
                == grid[row_index][column_index + 2] + grid[row_index + 1][column_index + 1] + grid[row_index + 2][column_index]
            ) and (
              set(grid[row_index][column_index:column_index + 3]) | set(grid[row_index + 1][column_index:column_index + 3]) | set(grid[row_index + 2][column_index:column_index + 3]) == Solution.MAGIC_DIGITS
            ))
