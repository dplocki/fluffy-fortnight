DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, columns = len(grid), len(grid[0])
        visited = set()

        for current_row, row in enumerate(grid):
            for current_column, cell_value in enumerate(row):
                if (current_row, current_column) in visited:
                    continue

                to_check = [(current_row, current_column, current_row, current_column)]
                while to_check:
                    r, c, pr, pc = to_check.pop()
                    if (r, c) in visited:
                        continue

                    visited.add((r, c))

                    for dr, dc in DIRECTIONS:
                        new_row = r + dr
                        new_column = c + dc

                        if not (0 <= new_row < rows) or not (0 <= new_column < columns) :
                            continue

                        if grid[new_row][new_column] != cell_value:
                            continue

                        if new_row == pr and new_column == pc:
                            continue

                        if (new_row, new_column) in visited:
                            return True

                        to_check.append((new_row, new_column, r, c))

        return False
