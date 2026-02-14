class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = { (0, 0): poured }

        for row in range(query_row + 1):
            for column in range(row + 1):
                current = glasses.get((row, column), 0.0)
                if current > 1.0:
                    glasses[row, column] = 1.0
                    half = (current - 1.0) / 2
                    glasses[row + 1, column] = half + glasses.get((row + 1, column), 0.0)
                    glasses[row + 1, column + 1] = half + glasses.get((row + 1, column + 1), 0.0)

        return min(1.0, glasses.get((query_row, query_glass), 0))
