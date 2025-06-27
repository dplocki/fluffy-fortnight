class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_queen_be_place(row, columns, current_column):
            for prev_row in range(row):
                if columns[row - prev_row - 1] in (current_column - prev_row - 1, prev_row + current_column + 1, current_column):
                    return False

            return True

        def internal(columns):
            row = len(columns)
            if row == n:
                yield 1
                return

            for column in range(n):
                if can_queen_be_place(row, columns, column):
                    yield from internal(columns + [column])

        return sum(internal([]))
