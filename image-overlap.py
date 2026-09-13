class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        img1_points = []
        img2_points = []

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    img1_points.append((r,c))

                if img2[r][c] == 1:
                    img2_points.append((r,c))

        result = 0
        diffs = defaultdict(int)
        for point1 in img1_points:
            for point2 in img2_points:
                dr = point1[0] - point2[0]
                dc = point1[1] - point2[1]

                diffs[dr, dc] += 1
                result = max(diffs[dr, dc], result)

        return result
