class Solution:
    MOD = 10**9 + 7

    def countTrapezoids(self, points: List[List[int]]) -> int:
            lines = defaultdict(set)

            for point in points:
                lines[point[1]].add(point[0])

            pairs_count = {}
            for y, points in lines.items():
                s = len(points)
                pairs_count[y] = s * (s - 1) >> 1

            return sum((a * b) % Solution.MOD for a, b in combinations(pairs_count.values(), 2))
