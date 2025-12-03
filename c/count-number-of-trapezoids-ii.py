class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slopes = defaultdict(set)
        corners = defaultdict(dict)
        midpoints = defaultdict(dict)

        for (x1, y1), (x2, y2) in combinations(points, r=2):
            slope = (y2 - y1) / (x2 - x1) if x1 != x2 else float('inf')

            slopes[slope].add(((x1, y1), (x2, y2)))
            corners[x1, y1][slope] = corners[x1, y1].get(slope, 0) + 1
            corners[x2, y2][slope] = corners[x2, y2].get(slope, 0) + 1
            mid = (x1 + x2) / 2, (y1 + y2) / 2
            midpoints[mid][slope] = midpoints[mid].get(slope, 0) + 1

        result = 0
        for slop in slopes:
            count = len(slopes[slop])
            if count < 2:
                continue

            for line in slopes[slop]:
                temp = corners[line[0]][slop]
                result += count - (temp * (temp + 1) // 2)

        result //= 2

        for midpoint in midpoints:
            total = sum(midpoints[midpoint].values())
            for slop in midpoints[midpoint]:
                current = midpoints[midpoint][slop]
                result -= (total - current) * current
                total -= current

        return result
