class Solution:
    MOD = 10**9 + 7

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        empty = [0] * k
        dp = {(0, 0): empty[:]}
        dp[0, 0][grid[0][0] % k] = 1

        for r_index, row in enumerate(grid):
            for c_index, cell_value in enumerate(row):
                if r_index == 0 and c_index == 0:
                    continue

                top = dp.get((r_index - 1, c_index), empty)
                left = dp.get((r_index, c_index - 1), empty)
                dp[r_index, c_index] = [0] * k
                
                for remainder in range(k):
                    new_remainder = (remainder + cell_value) % k
                    dp[r_index, c_index][new_remainder] = (top[remainder] + left[remainder]) % Solution.MOD

        return dp[len(grid) - 1, len(grid[0]) - 1][0]
