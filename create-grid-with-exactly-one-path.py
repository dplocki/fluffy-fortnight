class Solution:
    def createGrid(self, rows: int, columns: int) -> list[str]:
        return ['.' + '#' * (columns - 1)] * (rows - 1) + ['.' * columns]
