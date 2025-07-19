class Solution:
    SIDE_SIZE = 9
    ALL_DIGITS = 9 * 9

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(Solution.SIDE_SIZE):
            for c in range(Solution.SIDE_SIZE):
                if board[r][c] == '.':
                    continue

                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boxes[(r // 3) * 3 + (c // 3)].add(board[r][c])

        def internal(index: int) -> bool:
            if index == Solution.ALL_DIGITS:
                return True

            row, column = divmod(index, Solution.SIDE_SIZE)
            if board[row][column] != '.':
                return internal(index + 1)

            for c in range(1, 10):
                digit = str(c)
                if digit in rows[row] or digit in columns[column] or digit in boxes[(row // 3) * 3 + (column // 3)]:
                    continue

                rows[row].add(digit)
                columns[column].add(digit)
                boxes[(row // 3) * 3 + (column // 3)].add(digit)

                board[row][column] = digit
                if internal(index + 1):
                    return True

                boxes[(row // 3) * 3 + (column // 3)].remove(digit)
                columns[column].remove(digit)
                rows[row].remove(digit)

            board[row][column] = '.'
            return False

        internal(0)
