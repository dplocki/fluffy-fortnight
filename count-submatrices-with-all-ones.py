class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        vertical_splites = {}
        for row_index, row in enumerate(mat):
            for column_index, value in enumerate(row):
                vertical_splites[row_index, column_index] = 0 if value == 0 else 1 + vertical_splites.get((row_index, column_index - 1), 0)

        return sum(
            sum(accumulate((vertical_splites.get((k, column_index), 0) for k in range(row_index, -1, -1)), min))
            for row_index, row in enumerate(mat)
            for column_index, value in enumerate(row)
        )
