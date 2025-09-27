class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(
            abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
            for x1, y1 in points
            for x2, y2 in points
            for x3, y3 in points) / 2
