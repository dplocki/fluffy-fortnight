class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dimensions_with_diagonal = ((l ** 2 + h ** 2, l, h) for l, h in dimensions)
        sorted_by_diagonal = sorted(dimensions_with_diagonal, key=lambda d: d[0], reverse=True)
        areas = map(lambda d: d[1] * d[2], takewhile(lambda d: d[0] == sorted_by_diagonal[0][0], sorted_by_diagonal))
        return max(areas)
