class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        result = 0

        vertical_splites = {}
        for row_index, row in enumerate(mat):
            for column_index, value in enumerate(row):
                vertical_splites[row_index, column_index] = 0 if value == 0 else 1 + vertical_splites.get((row_index, column_index - 1), 0)

        for row_index, row in enumerate(mat):
            for column_index, value in enumerate(row):
                local_result = vertical_splites[row_index, column_index]
                result += local_result

                for k in range(row_index - 1, -1, -1):
                    local_result = min(local_result, vertical_splites.get((k, column_index), 0))
                    result += local_result

        return result
