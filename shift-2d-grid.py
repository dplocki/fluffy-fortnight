class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])
        all_cells = rows * columns

        result = [[0] * columns for _ in range(rows)]
        for row_index in range(rows):
            for column_index in range(columns):
                tmp = (columns * row_index + column_index + k) % all_cells
                result[tmp // columns][tmp % columns] = grid[row_index][column_index]

        return result
