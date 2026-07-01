DIR = ((0, -1), (0, 1), (1, 0), (-1, 0))

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thieves = [
            (row_index, column_index)
            for row_index, row in enumerate(grid)
            for column_index, cell in enumerate(row)
            if cell == 1
        ]

        @cache
        def get_safeness_factor(row_index: int, column_index: int) -> int:
            return min(
                abs(row_index - thief_row) + abs(column_index - thief_column)
                for thief_row, thief_column in thieves
            )

        to_check = []
        result = { (0, 0): get_safeness_factor(0, 0) }
        heappush(to_check, (result[0, 0], 0, 0))

        while to_check:
            current_path_safeness_factor, row_index, column_index = heappop(to_check)

            for drow, dcolumn in DIR:
                new_row_index, new_column_index = row_index + drow, column_index + dcolumn
                if (0 <= new_row_index < n) and (0 <= new_column_index < n) and ((new_row_index, new_column_index) not in result or result[new_row_index, new_column_index] < current_path_safeness_factor):
                    new_path_safeness_factor = min(current_path_safeness_factor, get_safeness_factor(new_row_index, new_column_index))
                    result[new_row_index, new_column_index] = new_path_safeness_factor
                    heappush(to_check, (new_path_safeness_factor, new_row_index, new_column_index))

        return result[n - 1, n - 1]
