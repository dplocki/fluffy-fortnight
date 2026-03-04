class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows, columns = {}, {}

        for row_index, row in enumerate(mat):
            for column_index, cell in enumerate(row):
                if cell == 0:
                    continue

                rows[row_index] = None if row_index in rows else column_index
                columns[column_index] = None if column_index in columns else row_index

        return sum(1
            for key, value in rows.items()
            if value != None and columns[value] != None)
