class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        max_row, max_column = len(dungeon), len(dungeon[0])
        end_position = max_row - 1, max_column - 1
        possibilities = [(0, 0, 0, 0)]
        result = []

        while possibilities:
            row, column, health_delta, required_health = possibilities.pop()

            health_delta += dungeon[row][column]
            required_health = min(required_health, health_delta)

            if (row, column) == end_position:
                result.append(abs(required_health) + 1 if required_health else 1)
                continue

            if row < max_row - 1:
                possibilities.append((row + 1, column, health_delta, required_health))

            if column < max_column - 1:
                possibilities.append((row, column + 1, health_delta, required_health))

        return min(result)
