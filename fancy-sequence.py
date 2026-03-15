class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.n = 0
        self.numbers = []
        self.inc = 0
        self.multiplayer = 1

    def append(self, val: int) -> None:
        self.numbers.append((val, self.inc, self.multiplayer))
        self.n += 1

    def addAll(self, inc: int) -> None:
        self.inc += inc

    def multAll(self, m: int) -> None:
        self.multiplayer = self.multiplayer * m % Fancy.MOD
        self.inc = self.inc * m % Fancy.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= self.n:
            return -1
        
        value, inc, multiplayer = self.numbers[idx]

        ratio = self.multiplayer * pow(multiplayer, Fancy.MOD - 2, Fancy.MOD)
        return (value * ratio + self.inc - ratio * inc) % Fancy.MOD
