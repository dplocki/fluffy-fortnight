class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = { i: set() for i in range(9) }
        columns = { i: set() for i in range(9) }
        boxes = { i: set() for i in range(9) }

        for row_index in range(9):
            for column_index in range(9):
                value = board[row_index][column_index]

                if value == '.':
                    continue
                
                if value in rows[row_index]:
                    return False

                rows[row_index].add(value)

                if value in columns[column_index]:
                    return False

                columns[column_index].add(value)

                box_index = (row_index // 3) * 3 + column_index // 3
                if value in boxes[box_index]:
                    return False

                boxes[box_index].add(value)

        return True

