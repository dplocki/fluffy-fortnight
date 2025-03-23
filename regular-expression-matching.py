class Solution:
    def isMatch(self, input_string: str, pattern: str) -> bool:
        table = { # row, column
            (input_index, pattern_index): False if input_index == 0 or pattern_index == 0 else None
            for input_index in range(len(input_string) + 1)
            for pattern_index in range(len(pattern) + 1)
        }

        table[0, 0] = True
        table_rows = len(input_string) + 1
        table_columns = len(pattern) + 1

        for row in range(table_rows):
            for column in range(1, table_columns):
                if pattern[column - 1] == '.':
                    if row == 0:
                        table[row, column] = False
                        continue

                    table[row, column] = table[row - 1, column - 1]
                    continue

                if pattern[column - 1] not in '.*':
                    if row == 0:
                        table[row, column] = False
                        continue

                    table[row, column] = (input_string[row - 1] == pattern[column - 1]) and (table[row - 1, column - 1])
                    continue

                if pattern[column - 1] == '*':
                    if row == 0:
                        table[row, column] = table[0, column - 2]
                        continue

                    table[row, column] = table[row, column - 2] or \
                        (pattern[column - 2] == '.' and table[row - 1, column]) or \
                        (pattern[column - 2] == input_string[row - 1] and table[row - 1, column])

                    continue

        return table[table_rows - 1, table_columns - 1]
