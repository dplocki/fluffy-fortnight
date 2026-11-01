DIRS = ((0, -1), (0, 1), (1, 0), (-1, 0))


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, columns = len(grid), len(grid[0])
        visited_land = set()


        def closed_island_value(row: int, column: int) -> int:
            result = 0
            to_visit = [(row, column)]
        
            while to_visit:
                r, c = to_visit.pop()

                if r < 0 or c < 0 or c >= columns or r >= rows:
                    continue

                if grid[r][c] <= 0:
                    continue

                if (r, c) in visited_land:
                    continue

                result += grid[r][c]

                visited_land.add((r, c))

                for dr, dc in DIRS:
                    to_visit.append((r + dr, c + dc))

            return result


        result = 0
        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                if value <= 0:
                    continue

                if (r, c) in visited_land:
                    continue

                if closed_island_value(r, c) % k == 0:
                    result += 1

        return result
