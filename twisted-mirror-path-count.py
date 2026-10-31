MOD = 10 ** 9 + 7

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        to_down = defaultdict(int)
        to_right = defaultdict(int)

        if grid[0][0] == 0:
            to_down[-1, 0] = 1
        else:
            to_down[-1, 0] = 1
            to_right[0, -1] = 1

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if grid[r][c] == 0:
                    all_sum = (to_down[r - 1, c] + to_right[r, c - 1]) % MOD
                    to_down[r, c] = all_sum
                    to_right[r, c] = all_sum
                else:
                    to_right[r, c] = to_down[r - 1, c]
                    to_down[r, c] = to_right[r, c - 1]

        return (to_down[rows - 2, columns - 1] + to_right[rows - 1, columns - 2]) % MOD
