class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        mark_as_immutable_cache = set()

        def mark_as_immutable(rindex: int, cindex: int):
            if (rindex, cindex) in mark_as_immutable_cache:
                return

            if rindex < 0 or rindex >= m or cindex < 0 or cindex >= n:
                return

            if board[rindex][cindex] == 'X':
                return

            mark_as_immutable_cache.add((rindex, cindex))

            mark_as_immutable(rindex - 1, cindex)
            mark_as_immutable(rindex + 1, cindex)
            mark_as_immutable(rindex, cindex - 1)
            mark_as_immutable(rindex, cindex + 1)

        for index in range(m):
            mark_as_immutable(index, 0)
            mark_as_immutable(index, n - 1)

        for index in range(n):
            mark_as_immutable(0, index)
            mark_as_immutable(m - 1, index)

        for rindex, row in enumerate(board):
            for cindex, c in enumerate(row):
                if board[rindex][cindex] == 'O' and (rindex, cindex) not in mark_as_immutable_cache:
                    board[rindex][cindex] = 'X'
