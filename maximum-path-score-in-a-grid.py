class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, columns = len(grid), len(grid[0])
        dp = {}

        @cache
        def internal(row: int, column: int, cost: int) -> int:
            if row >= rows or column >= columns:
                return -1

            new_cost = cost + (grid[row][column] > 0)
            if new_cost > k:
                return -1

            if row == rows - 1 and column == columns - 1:
                return grid[row][column]

            down = internal(row + 1, column, new_cost)
            right = internal(row, column + 1, new_cost)

            if down == -1 and right == -1:
                return -1

            return max(down, right) + grid[row][column]

        try:
            return internal(0, 0, 0)
        finally:
            internal.cache_clear()
