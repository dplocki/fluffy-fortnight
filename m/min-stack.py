class MinStack:

    def __init__(self):
        self.memory = []
        self.minims = []

    def push(self, val: int) -> None:
        self.memory.append(val)

        if not self.minims or val <= self.minims[-1]:
            self.minims.append(val)

    def pop(self) -> None:
        val = self.memory.pop()

        if self.minims and val == self.minims[-1]:
            self.minims.pop()

    def top(self) -> int:
        return self.memory[-1]

    def getMin(self) -> int:
        if self.minims:
            return self.minims[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
