class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        return max(
            n - 1 - next(i for i in range(n) if colors[i] != colors[-1]), 
            next(i for i in range(n - 1, -1, -1) if colors[i] != colors[0]), 
        )
