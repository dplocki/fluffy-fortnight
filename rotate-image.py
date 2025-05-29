class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for row in range(size // 2):
            for column in range(size):
                matrix[row][column], matrix[size - row - 1][column] = matrix[size - row - 1][column], matrix[row][column]

        for row in range(size):
            for column in range(row):
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
