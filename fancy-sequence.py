class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.n = 0
        self.operations_number = 0
        self.numbers = []
        self.operations = []

    def append(self, val: int) -> None:
        self.numbers.append((val, self.operations_number))
        self.n += 1

    def addAll(self, inc: int) -> None:
        self.operations.append(lambda x: (x + inc) % Fancy.MOD)
        self.operations_number += 1

    def multAll(self, m: int) -> None:
        self.operations.append(lambda x: (x * m) % Fancy.MOD)
        self.operations_number += 1

    def getIndex(self, idx: int) -> int:
        if idx >= self.n:
            return -1

        result, operation_start = self.numbers[idx]
        for operation_index in range(operation_start, self.operations_number):
            result = self.operations[operation_index](result)

        return result
