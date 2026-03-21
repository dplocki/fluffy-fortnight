class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for sri in range(k >> 1):
            for sci in range(k):
                grid[x + sri][y + sci], grid[x + (k - sri - 1)][y + sci] = grid[x + (k - sri - 1)][y + sci], grid[x + sri][y + sci]

        return grid
