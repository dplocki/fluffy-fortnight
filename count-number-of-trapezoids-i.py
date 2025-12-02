class Solution:
    MOD = 10**9 + 7

    def countTrapezoids(self, points: List[List[int]]) -> int:
        lines = defaultdict(int)

        for point in points:
            lines[point[1]] += 1

        pairs_count = (
            s * (s - 1) >> 1
            for y, s in lines.items()
        )

        return sum((a * b) % Solution.MOD for a, b in combinations(pairs_count, 2))
