class Solution:
    SIDE_SIZE = 9
    ALL_DIGITS = 9 * 9

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_correct(digits):
            seen = set()
            for item in digits:
                if item == '.':
                    continue

                if item in seen:
                    return False

                seen.add(item)

            return True

        def check_element(row: int, column: int) -> bool:
            return is_correct(board[row]) and \
                is_correct(board[i][column] for i in range(Solution.SIDE_SIZE)) and \
                is_correct(
                    board[(row // 3) * 3 + r][(column // 3) * 3 + c]
                    for c in range(3)
                    for r in range(3)
                )

        def internal(index: int) -> bool:
            if index == Solution.ALL_DIGITS:
                return True

            row, column = divmod(index, Solution.SIDE_SIZE)
            if board[row][column] != '.':
                return internal(index + 1)

            for c in range(1, 10):
                board[row][column] = str(c)

                if check_element(row, column) and internal(index + 1):
                    return True

            board[row][column] = '.'
            return False

        internal(0)
