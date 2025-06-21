class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for _ in range(rowIndex):
            row = [1]

            for l, r in zip(prev, prev[1:]):
                row.append(l + r)
            
            row.append(1)
            prev = row

        return prev
