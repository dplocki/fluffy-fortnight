class Solution:
    SIDE_SIZE = 9
    ALL_DIGITS = 9 * 9
    DIGITS = '123456789'

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == '.':
                    continue

                rows[r].add(cell)
                columns[c].add(cell)
                boxes[(r // 3) * 3 + (c // 3)].add(cell)

        def internal(index: int) -> bool:
            if index == Solution.ALL_DIGITS:
                return True

            row, column = divmod(index, Solution.SIDE_SIZE)
            if board[row][column] != '.':
                return internal(index + 1)

            box_index = (row // 3) * 3 + (column // 3)
            for digit in Solution.DIGITS:
                if digit in rows[row] or digit in columns[column] or digit in boxes[box_index]:
                    continue

                rows[row].add(digit)
                columns[column].add(digit)
                boxes[box_index].add(digit)

                board[row][column] = digit
                if internal(index + 1):
                    return True

                boxes[box_index].remove(digit)
                columns[column].remove(digit)
                rows[row].remove(digit)

            board[row][column] = '.'
            return False

        internal(0)
