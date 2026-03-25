class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, columns = 0, 0
        prefix_table = {}

        for r, row in enumerate(grid):
            rows += 1
            columns = 0

            for c, cell in enumerate(row):
                columns += 1
                prefix_table[r, c] = cell + prefix_table.get((r - 1, c), 0) + prefix_table.get((r, c - 1), 0) - prefix_table.get((r - 1, c - 1), 0)

        whole_sum = prefix_table[rows - 1, columns - 1]

        for r in range(1, rows):
            if (prefix_table[r - 1, columns - 1] << 1) == whole_sum:
                return True
    
        for c in range(1, columns):
            if (prefix_table[rows - 1, c - 1] << 1) == whole_sum:
                return True

        return False
