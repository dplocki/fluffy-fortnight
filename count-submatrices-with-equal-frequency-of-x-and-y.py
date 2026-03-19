class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        previous_row = { -1: (0, 0) }

        for c in range(columns):
            previous_row[c] = (0, 0)

        result = 0
        for row in grid:
            current_row = { -1: (0, 0) }

            for c, cell in enumerate(row):
                x1, y1 = previous_row[c - 1]
                x2, y2 = previous_row[c]
                x3, y3 = current_row[c - 1]

                x = x2 + x3 + (1 if cell == 'X' else 0) - x1
                y = y2 + y3 + (1 if cell == 'Y' else 0) - y1

                current_row[c] = (x, y)

                if x > 0 and x == y:
                    result += 1

            previous_row = current_row

        return result
