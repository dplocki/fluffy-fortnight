DIRECTIONS_LABELS = ("North", "East", "South", "West")

class Robot:

    def __init__(self, width: int, height: int):
        self.x, self.y, self.directory = 0, 0, 1
        self.index = 0
        self.whole_border = 2 * width + 2 * height - 4
        self.border = { 0: (0, 0, 2) }

        index = 0
        for i in range(1, width):
            index += 1
            self.border[index] = (i, 0, 1)

        for i in range(1, height):
            index += 1
            self.border[index] = (width - 1, i, 0)

        for i in range(width - 2, -1, -1):
            index += 1
            self.border[index] = (i, height - 1, 3)

        for i in range(height - 2, 0, -1):
            index += 1
            self.border[index] = (0, i, 2)

    def step(self, num: int) -> None:
        if num == 0:
            return

        self.index = (self.index + num) % self.whole_border
        self.x, self.y, self.directory = self.border[self.index]

    def getPos(self) -> List[int]:
        return self.x, self.y

    def getDir(self) -> str:
        return DIRECTIONS_LABELS[self.directory]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
