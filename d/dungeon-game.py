class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        max_row, max_column = len(dungeon), len(dungeon[0])
        results = {
            (max_row, max_column - 1): 1,
            (max_row - 1, max_column): 1
        }

        for row in range(max_row - 1, -1, -1):
            for column in range(max_column - 1, -1, -1):
                results[row, column] = max(1, min(results.get((row + 1, column), inf), results.get((row, column + 1), inf)) - dungeon[row][column])

        return results[0, 0]
