class Solution:
    DIRS = {
        0: (0, 1),
        1: (1, 0),
        2: (0, -1),
        3: (-1, 0),
    }

    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        result = []

        for _ in range(n):
            result.append([0] * n)

        for column in range(n):
            result[0][column] = column + 1

        direction = 1
        drow, dcolumn = self.DIRS[direction]
        row, column = 0, n - 1
        step = n - 1
        current = n + 1

        while step > 0:
            for _ in range(step):
                row += drow
                column += dcolumn
                result[row][column] = current
                current += 1

            direction = (direction + 1) % 4
            drow, dcolumn = self.DIRS[direction]

            for _ in range(step):
                row += drow
                column += dcolumn
                result[row][column] = current
                current += 1

            direction = (direction + 1) % 4
            drow, dcolumn = self.DIRS[direction]

            step -= 1

        return result
