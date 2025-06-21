class Solution:
    def isMatch(self, input_string: str, pattern: str) -> bool:
        table_rows = len(input_string) + 1
        table_columns = len(pattern) + 1

        table = { # row, column
            (input_index, pattern_index): False if input_index == 0 or pattern_index == 0 else None
            for input_index in range(table_rows)
            for pattern_index in range(table_columns)
        }

        table[0, 0] = True
        for column in range(1, table_columns):
            if pattern[column - 1] == '*':
                table[0, column] = table[0, column - 2]
            else:
                table[0, column] = False

        for row in range(1, table_rows):
            for column in range(1, table_columns):
                if pattern[column - 1] == '.':
                    table[row, column] = table[row - 1, column - 1]
                elif pattern[column - 1] == '*':
                    table[row, column] = table[row, column - 2] or \
                        (pattern[column - 2] == '.' and table[row - 1, column]) or \
                        (pattern[column - 2] == input_string[row - 1] and table[row - 1, column])
                else:
                    table[row, column] = (input_string[row - 1] == pattern[column - 1]) and (table[row - 1, column - 1])

        return table[table_rows - 1, table_columns - 1]
