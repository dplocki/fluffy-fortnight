MOD = 10 ** 9 + 7

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        matrix_size = 2 * m

        def multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
            C = [[0] * matrix_size for _ in range(matrix_size)]

            for i in range(matrix_size):
                for k in range(matrix_size):
                    if A[i][k] == 0:
                        continue

                    current = A[i][k]

                    for j in range(matrix_size):
                        if B[k][j] == 0:
                            continue

                        C[i][j] = (C[i][j] + current * B[k][j]) % MOD

            return C


        T = [[0] * matrix_size for _ in range(matrix_size)]

        for x in range(m):

            for y in range(x + 1, m):
                T[x][m + y] = 1

            for y in range(x):
                T[m + x][y] = 1

        result = [[0] * matrix_size for _ in range(matrix_size)]
        for i in range(matrix_size):
            result[i][i] = 1

        power = n - 1

        while power:
            if power & 1:
                result = multiply(result, T)

            T = multiply(T, T)
            power >>= 1

        answer = 0

        for i in range(matrix_size):
            row_sum = sum(result[i]) % MOD
            answer = (answer + row_sum) % MOD

        return answer
