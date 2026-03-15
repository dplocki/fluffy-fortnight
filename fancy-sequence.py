class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.n = 0
        self.numbers = []

    def append(self, val: int) -> None:
        self.numbers.append(val)
        self.n += 1

    def addAll(self, inc: int) -> None:
        for index, number in enumerate(self.numbers):
            self.numbers[index] = (number + inc) % Fancy.MOD

    def multAll(self, m: int) -> None:
        for index, number in enumerate(self.numbers):
            self.numbers[index] = (number * m) % Fancy.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= self.n:
            return -1

        return self.numbers[idx]
