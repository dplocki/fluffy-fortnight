class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        xs = set()
        ys = set()
        
        for row_index, row in enumerate(grid):
            for column_index, cell in enumerate(row):
                if cell == 1:
                    xs.add(row_index)
                    ys.add(column_index)

        return (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)
