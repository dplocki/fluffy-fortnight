class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_length = len(word)
        rows_length = len(board)
        columns_length = len(board[0])

        for possibility in (
                (row_index, column_index)
                for row_index, row in enumerate(board)
                for column_index, character in enumerate(row)
                if character == word[0]):
            paths = [(possibility, {possibility})]
            
            while paths:
                position, previous_positions = paths.pop()
                current_match_lenght = len(previous_positions)
                if current_match_lenght == word_length:
                    return True

                row, column = position
                for new_postion_row, new_postion_col, in ((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)):
                    if (new_postion_row, new_postion_col) in previous_positions:
                        continue

                    if new_postion_row < 0 or new_postion_row >= rows_length:
                        continue

                    if new_postion_col < 0 or new_postion_col >= columns_length:
                        continue

                    if word[current_match_lenght] == board[new_postion_row][new_postion_col]:
                        paths.append(((new_postion_row, new_postion_col), previous_positions | {(new_postion_row, new_postion_col)}))

        return False
