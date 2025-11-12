class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a, b = abs(z - x), abs(z - y)
        return 2 if a > b else 0 if a == b else 1
