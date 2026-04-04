class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        columns = len(encodedText) // rows
        result = ''
        if encodedText == '':
            return ''
        
        r, c, cs = 0, 0, 0
        while r < rows or c < columns:
            result += encodedText[r * columns + c]
            c += 1
            r += 1

            if r == rows:
                r = 0
                cs += 1
                c = cs
            
            if c == columns:
                break

                    
        return result.rstrip()
