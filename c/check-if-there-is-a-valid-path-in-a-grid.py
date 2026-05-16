DIRECTIONS_COUNT = 4
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0 up, 1 right, 2 down, 3 left
TILES_MAP = {
    1: (1, 3),
    2: (0, 2),
    3: (2, 3),
    4: (1, 2),
    5: (0, 3),
    6: (0, 1)
}

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        def check(row: int, column: int) -> bool:
            return (0 <= row < m) and (0 <= column < n)


        visited = set()
        to_check = [(0, 0)]

        while to_check:
            current_row, current_column = to_check.pop()
            if (current_row, current_column) in visited:
                continue

            if current_row == m - 1 and current_column == n - 1:
                return True

            visited.add((current_row, current_column))
            current_cell = grid[current_row][current_column]

            for e in TILES_MAP[current_cell]:
                dr, dc = DIRECTIONS[e]
                new_row, new_column = current_row + dr, current_column + dc

                if not check(new_row, new_column):
                    continue

                if ((e + 2) % DIRECTIONS_COUNT) not in TILES_MAP[grid[new_row][new_column]]:
                    continue

                to_check.append((new_row, new_column))

        return False
