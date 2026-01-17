class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        return max(
            filter(
                lambda e: e > 0,
                (
                    min(min(e1_x, e2_x) - max(s1_x, s2_x), min(e1_y, e2_y) - max(s1_y, s2_y))
                    for ((s1_x, s1_y), (e1_x, e1_y)), ((s2_x, s2_y), (e2_x, e2_y)) in combinations(zip(bottomLeft, topRight), 2)
                )
            ),
            default = 0
        ) ** 2
