class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])


        def rotate_cell(row: int, column: int) -> Tuple[int, int]:
            layer_id = min(row, column, rows - 1 - row, columns - 1 - column)
            layer_rows = rows - layer_id * 2
            layer_columns = columns - layer_id * 2
            layer_border = (layer_rows - 1) * 2 + (layer_columns - 1) * 2

            top_row = layer_id
            bottom_row = rows - 1 - layer_id
            left_column = layer_id
            right_column = columns - 1 - layer_id

            if row == top_row:
                place_on_ring = column - left_column
            elif column == right_column:
                place_on_ring = (layer_columns - 1) + (row - top_row)
            elif row == bottom_row:
                place_on_ring = (layer_columns - 1) + (layer_rows - 1) + (right_column - column)
            else:
                place_on_ring = (layer_columns - 1) + (layer_rows - 1) + (layer_columns - 1) + (bottom_row - row)

            new_place = (place_on_ring - k) % layer_border

            if new_place < layer_columns:
                return top_row, left_column + new_place
            new_place -= layer_columns - 1
            if new_place < layer_rows:
                return top_row + new_place, right_column
            new_place -= layer_rows - 1
            if new_place < layer_columns:
                return bottom_row, right_column - new_place
            new_place -= layer_columns - 1
            return bottom_row - new_place, left_column


        result = [[None] * columns for _ in range(rows)]
        for row_index, row in enumerate(grid):
            for column_index, value in enumerate(row):
                r, c = rotate_cell(row_index, column_index)
                result[r][c] = value

        return result
