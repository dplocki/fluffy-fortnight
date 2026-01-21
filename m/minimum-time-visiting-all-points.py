class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(
            max(abs(p1_x - p2_x), abs(p1_y - p2_y))
            for (p1_x, p1_y), (p2_x, p2_y) in zip(points, points[1:]))
