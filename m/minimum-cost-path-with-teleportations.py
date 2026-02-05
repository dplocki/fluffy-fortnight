class Solution:
    INFINITY = float('inf')

    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = { (0, 0, 0): 0 }
        weights_map = {}

        for ri, row in enumerate(grid):
            for ci, value in enumerate(row):
                if ci:
                    dp[ri, ci, 0] = min(
                        dp.get((ri, ci, 0), Solution.INFINITY),
                        dp.get((ri, ci - 1, 0), Solution.INFINITY) + grid[ri][ci]
                    )
                if ri:
                    dp[ri, ci, 0] = min(
                        dp.get((ri, ci, 0), Solution.INFINITY),
                        dp.get((ri - 1, ci, 0), Solution.INFINITY) + grid[ri][ci]
                    )

                if value not in weights_map:
                    weights_map[value] = []
                
                weights_map[value].append((ri, ci))

        weights = sorted(weights_map, reverse=True)
        for teleportation in range(1, k + 1):
            minium_cost = Solution.INFINITY
            for weight in weights:
                minium_cost = min(
                    minium_cost,
                    min(dp[ri, ci, teleportation - 1] for ri, ci in weights_map[weight])
                )

                for ri, ci in weights_map[weight]:
                    dp[ri, ci, teleportation] = minium_cost

            for ri, row in enumerate(grid):
                for ci, value in enumerate(row):
                    if ci:
                        dp[ri, ci, teleportation] = min(
                            dp.get((ri, ci, teleportation), Solution.INFINITY),
                            dp.get((ri, ci - 1, teleportation), Solution.INFINITY) + value
                        )
                    if ri:
                        dp[ri, ci, teleportation] = min(
                            dp.get((ri, ci, teleportation), Solution.INFINITY),
                            dp.get((ri - 1, ci, teleportation), Solution.INFINITY) + value
                        )

        return min(dp.get((m - 1, n - 1, t), Solution.INFINITY) for t in range(k + 1))
