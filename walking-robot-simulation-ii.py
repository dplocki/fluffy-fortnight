DIRECTIONS = { 0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0) }
DIRECTIONS_LABELS = ("North", "East", "South", "West")

class Robot:

    def __init__(self, width: int, height: int):
        self.directory = 1
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        dx, dy = DIRECTIONS[self.directory]

        for _ in range(num):
            tx = self.x + dx
            ty = self.y + dy
            if not ((0 <= tx < self.width) and (0 <= ty < self.height)):
                self.directory = (self.directory - 1) % 4
                dx, dy = DIRECTIONS[self.directory]
                self.x += dx
                self.y += dy
            else:
                self.x = tx
                self.y = ty

    def getPos(self) -> List[int]:
        return (self.x, self.y)

    def getDir(self) -> str:
        return DIRECTIONS_LABELS[self.directory]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
