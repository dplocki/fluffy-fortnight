class Solution:
    MOD = 12345

    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])
        result = [[0] * columns for _ in range(rows)]

        suffix_product = 1
        for r in range(rows - 1, - 1, -1):
            for c in range(columns - 1, - 1, -1):
                result[r][c] = suffix_product
                suffix_product = (suffix_product * grid[r][c]) % Solution.MOD

        prefix_product = 1
        for r in range(rows):
            for c in range(columns):
                result[r][c] = (result[r][c] * prefix_product) % Solution.MOD
                prefix_product = (prefix_product * grid[r][c]) % Solution.MOD

        return result
