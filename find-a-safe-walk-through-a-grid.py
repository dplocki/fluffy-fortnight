DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n, m = len(grid), len(grid[0])
        visited = {}
        to_check = [(0, 0, health - grid[0][0])]

        while to_check:
            current_row, current_column, current_health = to_check.pop()
            if current_row == n - 1 and current_column == m - 1:
                return True

            if (current_row, current_column) in visited and visited[current_row, current_column] > current_health:
                continue

            visited[current_row, current_column] = current_health

            for drow, dcolumn in DIR:
                new_row, new_column = current_row + drow, current_column + dcolumn
                if not (0 <= new_row < n and 0 <= new_column < m):
                    continue

                new_health = current_health - grid[new_row][new_column]
                if new_health <= 0:
                    continue

                if (new_row, new_column) not in visited or visited[new_row, new_column] < new_health:
                    to_check.append((new_row, new_column, new_health))

        return False
