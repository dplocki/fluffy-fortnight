class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp0 = [0] * (n + 1)
        dp1 = [0] * (n + 1)

        for j in range(1, n):
            new_dp0 = [0] * (n + 1)
            new_dp1 = [0] * (n + 1)

            for i in range(n + 1):
                previous = 0
                current = sum(grid[x][j] for x in range(i))

                for y in range(n + 1):
                    if y > 0 and y <= i:
                        current -= grid[y - 1][j]

                    if j > 0 and y > i:
                        previous += grid[y - 1][j - 1]

                    new_dp0[y] = max(new_dp0[y], previous + dp0[i], dp1[i])
                    new_dp1[y] = max(new_dp1[y], current + dp1[i], current + previous + dp0[i])

            dp0, dp1 = new_dp0, new_dp1

        return max(dp1)
