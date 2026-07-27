DIR = ((0, -1), (0, 1), (1, 0), (-1, 0))

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        safeness = {}
        to_checked = deque()

        for row in range(n):
            for column in range(n):
                if grid[row][column] == 1:
                    safeness[row, column] = 0
                    to_checked.append((row, column))

        while to_checked:
            row, column = to_checked.popleft()
            for drow, dcolumn in DIR:
                new_row, new_column = row + drow, column + dcolumn
                if 0 <= new_row < n and 0 <= new_column < n and (new_row, new_column) not in safeness:
                    safeness[new_row, new_column] = safeness[row, column] + 1
                    to_checked.append((new_row, new_column))

        distance = {}
        distance[0, 0] = safeness[0, 0]
        max_heap = [(-distance[0, 0], 0, 0)]

        while max_heap:
            neg_safe_factor, row, column = heapq.heappop(max_heap)
            safe_factor = -neg_safe_factor
            if safe_factor < distance.get((row, column), -1):
                continue

            if (row, column) == (n - 1, n - 1):
                return safe_factor

            for drow, dcolumn in DIR:
                new_row, new_column = row + drow, column + dcolumn
                if 0 <= new_row < n and 0 <= new_column < n:
                    new_safe_factor = min(safe_factor, safeness[new_row, new_column])
                    if new_safe_factor > distance.get((new_row, new_column), -1):
                        distance[new_row, new_column] = new_safe_factor
                        heapq.heappush(max_heap, (-new_safe_factor, new_row, new_column))

        return distance[n - 1][n - 1]
