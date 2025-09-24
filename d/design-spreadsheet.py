class Spreadsheet:

    def __init__(self, rows: int):
      self.cells = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells[cell] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+')
        a = int(a) if a.isnumeric() else self.cells[a]
        b = int(b) if b.isnumeric() else self.cells[b]

        return a + b

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
