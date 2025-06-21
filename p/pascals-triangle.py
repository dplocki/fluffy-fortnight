class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        prev = [1]
        for _ in range(numRows - 1):
            row = [1]

            for l, r in zip(prev, prev[1:]):
                row.append(l + r)
            
            row.append(1)

            result.append(row)
            prev = row

        return result
