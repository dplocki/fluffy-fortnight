ROCK, OBSTACLE, EMPTY = '#', '*', '.'

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        result = [[EMPTY] * m for _ in range(n)]

        for r in range(m):
            last_aviable_position = n - 1
            for c in range(n - 1, -1, -1):
                cell = boxGrid[r][c]
                if cell == ROCK:
                    result[last_aviable_position][m - r - 1] = ROCK
                    last_aviable_position -= 1
                elif cell == OBSTACLE:
                    result[c][m - r - 1] = OBSTACLE
                    last_aviable_position = c - 1
    
        return result
