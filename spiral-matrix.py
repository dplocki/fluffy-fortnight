DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return list(self.traverse(matrix))

    def traverse(self, matrix):
        rows_size, columns_size = len(matrix) - 1, len(matrix[0])
        r, c, d = 0, -1, 0

        while True:
            if columns_size == 0:
                return

            for _ in range(columns_size):
                r += DIR[d][0]
                c += DIR[d][1]
                yield matrix[r][c]
            
            columns_size -= 1
            d = (d + 1) % 4

            if rows_size == 0:
                return

            for _ in range(rows_size):
                r += DIR[d][0]
                c += DIR[d][1]
                yield matrix[r][c]

            rows_size -= 1
            d = (d + 1) % 4
