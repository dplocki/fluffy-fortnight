class MinStack:

    def __init__(self):
        self.memory = []

    def push(self, val: int) -> None:
        self.memory.append(val)

    def pop(self) -> None:
        self.memory.pop()

    def top(self) -> int:
        return self.memory[-1]

    def getMin(self) -> int:
        return min(self.memory)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
