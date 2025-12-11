class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        top = {}
        bottom = {}
        left = {}
        right = {}

        for row, column in buildings:
            top[column] = min(top.get(column, n), row)
            bottom[column] = max(bottom.get(column, 0), row)

            left[row] = min(left.get(row, n), column)
            right[row] = max(right.get(row, 0), column)

        return sum(1
            for row, column in buildings
            if ((left[row] < column < right[row]) and (top[column] < row < bottom[column])))
