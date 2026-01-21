class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        horizontal = {}
        vertical = {}

        for c in range(n):
            for r in range(m):
                horizontal[r, c] = horizontal.get((r, c - 1), 0) + grid[r][c]
                vertical[r, c] = vertical.get((r - 1, c), 0) + grid[r][c]

        for size in range(min(m, n), 1, -1):
            for c in range(n - size + 1):
                for r in range(m - size + 1):
                    lines = set(
                        horizontal.get((r + s, c + size - 1), 0) - horizontal.get((r + s, c - 1), 0)
                        for s in range(size))

                    if len(lines) != 1:
                        continue

                    columns = set(
                        vertical.get((r + size - 1, c + s), 0) - vertical.get((r - 1, c + s), 0)
                        for s in range(size))
                    
                    if len(columns) != 1:
                        continue

                    if lines != columns:
                        continue

                    magic_sum = lines.pop()
                    if sum(grid[r + i][c + i] for i in range(size)) != magic_sum:
                        continue

                    if sum(grid[r + i][c + size - 1 - i] for i in range(size)) != magic_sum:
                        continue

                    return size

        return 1
