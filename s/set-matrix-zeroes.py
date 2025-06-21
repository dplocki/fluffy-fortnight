class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_is_zeros = any(cell == 0 for cell in matrix[0])
        first_column_is_zeros = any(row[0] == 0 for row in matrix)

        for row_index, row in enumerate(matrix):
            for column_index, cell in enumerate(row):
                if cell == 0:
                    matrix[0][column_index] = 0
                    matrix[row_index][0] = 0

        for row_index in range(1, len(matrix)):
            for column_index in range(1, len(matrix[0])):
                if matrix[0][column_index] == 0 or matrix[row_index][0] == 0:
                    matrix[row_index][column_index] = 0

        if first_row_is_zeros:
            for column_index in range(len(matrix[0])):
                matrix[0][column_index] = 0
            
        if first_column_is_zeros:
            for row_index in range(len(matrix)):
                matrix[row_index][0] = 0
