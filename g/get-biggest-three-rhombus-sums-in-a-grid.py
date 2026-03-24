class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
      
        diagonal_sum_down_right = {}
        diagonal_sum_down_left = {}
      
        for r, row in enumerate(grid, 1):
            for c, value in enumerate(row, 1):
                diagonal_sum_down_right[r, c] = diagonal_sum_down_right.get((r - 1, c - 1), 0) + value
                diagonal_sum_down_left[r, c] = diagonal_sum_down_left.get((r - 1, c + 1), 0) + value
      
        unique_sums = SortedSet()
      
        for r, row in enumerate(grid, 1):
            for c, center_value in enumerate(row, 1):
                max_radius = min(r - 1, n - r, c - 1, m - c)
                unique_sums.add(center_value)
              
                for radius in range(1, max_radius + 1):
                    top_right_edge = diagonal_sum_down_right[r + radius, c] - diagonal_sum_down_right[r, c - radius]
                    bottom_right_edge = diagonal_sum_down_right[r, c + radius] - diagonal_sum_down_right[r - radius, c]
                    top_left_edge = diagonal_sum_down_left[r, c - radius] - diagonal_sum_down_left[r - radius, c]
                    bottom_left_edge = diagonal_sum_down_left[r + radius, c] - diagonal_sum_down_left[r, c + radius]
                  
                    rhombus_sum = top_right_edge + bottom_right_edge + top_left_edge + bottom_left_edge - grid[r + radius - 1][c - 1] + grid[r - radius - 1][c - 1]

                    unique_sums.add(rhombus_sum)
              
                while len(unique_sums) > 3:
                    unique_sums.remove(unique_sums[0])
      
        return unique_sums[::-1]
