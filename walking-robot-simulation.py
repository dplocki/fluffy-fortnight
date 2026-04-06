class Solution:
    DIRECTIONS = { 0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0) }

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, direction = 0, 0, 0
        obstacles = set(map(tuple, obstacles))
        result = 0

        for command in commands:
            if command == -2:
                direction = (direction - 1) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                dx, dy = Solution.DIRECTIONS[direction]
                for _ in range(command):
                    tx = x + dx
                    ty = y + dy
                    if (tx, ty) in obstacles:
                        break

                    x, y = tx, ty
                    result = max(result, x ** 2 + y ** 2)

        return result
