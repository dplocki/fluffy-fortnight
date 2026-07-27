MOD = 10**9 + 7

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        board = {
            (ri, ci): int(c)
            for ri, row in enumerate(board)
            for ci, c in enumerate(row)
            if c != 'X' and c != 'E' and c != 'S'
        }
        board[0, 0] = 0 # 'S'
        board[n - 1, n - 1] = 0 # 'E'

        dp_sum = defaultdict(int)
        dp_sum[n - 1, n - 1] = 0
        dp_paths = defaultdict(int)
        dp_paths[n - 1, n - 1] = 1

        for row in range(n - 1, -1, -1):
            for column in range(n - 1, -1, -1):
                if (row, column) not in board or (dp_paths[row, column] == 0):
                    dp_sum[row, column] = 0
                    dp_paths[row, column] = 0
                    continue

                if (row - 1, column) in board:
                    new_value = (dp_sum[row, column] + board[row - 1, column]) % MOD
                    if new_value > dp_sum[row - 1, column]:
                        dp_sum[row - 1, column] = new_value
                        dp_paths[row - 1, column] = dp_paths[row, column]
                    elif new_value == dp_sum[row - 1, column]:
                        dp_paths[row - 1, column] += dp_paths[row, column]
                        dp_paths[row - 1, column] %= MOD

                if (row, column - 1) in board:
                    new_value = (dp_sum[row, column] + board[row, column - 1]) % MOD
                    if new_value > dp_sum[row, column - 1]:
                        dp_sum[row, column - 1] = new_value
                        dp_paths[row, column - 1] = dp_paths[row, column]
                    elif new_value == dp_sum[row, column - 1]:
                        dp_paths[row, column - 1] += dp_paths[row, column]
                        dp_paths[row, column - 1] %= MOD

                if (row - 1, column - 1) in board:
                    new_value = (dp_sum[row, column] + board[row - 1, column - 1]) % MOD
                    if new_value > dp_sum[row - 1, column - 1]:
                        dp_sum[row - 1, column - 1] = new_value
                        dp_paths[row - 1, column - 1] = dp_paths[row, column]
                    elif new_value == dp_sum[row - 1, column - 1]:
                        dp_paths[row - 1, column - 1] += dp_paths[row, column]
                        dp_paths[row - 1, column - 1] %= MOD

        return (dp_sum[0, 0], dp_paths[0, 0])
