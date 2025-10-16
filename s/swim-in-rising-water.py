class Solution:
    DIRS = ((0, -1), (0, 1), (1, 0), (-1, 0))

    def swimInWater(self, grid: List[List[int]]) -> int:
        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression

            return parent[node]

        n = len(grid) 
        parent = list(range(n * n)) 
        elevation_to_position = [0] * (n * n)

        for row_index, row in enumerate(grid):
            for col_index, elevation in enumerate(row):
                elevation_to_position[elevation] = row_index * n + col_index

        for time in range(n * n):
            current_cell_idx = elevation_to_position[time]
            current_row = current_cell_idx // n
            current_col = current_cell_idx % n

            for delta_row, delta_col in Solution.DIRS:
                neighbor_row = current_row + delta_row
                neighbor_col = current_col + delta_col

                if (0 <= neighbor_row < n and 
                    0 <= neighbor_col < n and 
                    grid[neighbor_row][neighbor_col] <= time):
                    neighbor_idx = neighbor_row * n + neighbor_col
                    parent[find(neighbor_idx)] = find(current_cell_idx)

                if find(0) == find(n * n - 1):
                    return time

        return -1
