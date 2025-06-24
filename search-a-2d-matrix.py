class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_count, columns_count = len(matrix), len(matrix[0])
        left, right = 0, rows_count * columns_count - 1

        while left < right:
            middle = (left + right) >> 1

            row = middle // columns_count
            column = middle % columns_count

            if matrix[row][column] >= target:
                right = middle
            else:
                left = middle + 1

        return matrix[left // columns_count][left % columns_count] == target
