class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = { i: '' for i in range(numRows) } 
        for row_index, character in zip(self.which_row(numRows), s):
            result[row_index] += character

        return ''.join(result[i] for i in range(numRows))
    
    def which_row(self, numRows: int):
        while True:
            for i in range(numRows):
                yield i

            for i in range(numRows - 2, 0, -1):
                yield i
