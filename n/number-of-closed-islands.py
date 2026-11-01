WATER = 1
LAND = 0 
DIRS = ((0, -1), (0, 1), (1, 0), (-1, 0))

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited_land = set()
        result = 0


        def is_closed_island(row: int, column: int) -> bool:
            result = True
            to_visit = [(row, column)]
        
            while to_visit:
                r, c = to_visit.pop()

                if r < 0 or c < 0 or c >= columns or r >= rows:
                    continue

                if grid[r][c] == WATER:
                    continue

                if (r, c) in visited_land:
                    continue

                visited_land.add((r, c))

                if result and (r == 0 or r == rows - 1 or c == 0 or c == columns - 1):
                    result = False

                for dr, dc in DIRS:
                    to_visit.append((r + dr, c + dc))

            return result


        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                if value == WATER:
                    continue

                if (r, c) in visited_land:
                    continue

                if is_closed_island(r, c):
                    result += 1

        return result
