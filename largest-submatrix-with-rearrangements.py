class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        consequite_ones = [matrix[0][:]] 

        for r, row in enumerate(matrix[1:], 1):
            consequite_ones.append([
                (consequite_ones[r - 1][c] + 1) if cell == 1 else 0
                for c, cell in enumerate(row)
            ])

        result = 0
        for row in consequite_ones:
            row.sort(reverse=True)

            for width, height in enumerate(row, 1):  
                result = max(width * height, result)

        return result


