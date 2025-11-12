class Solution:
    DIRS = ((0,1), (0, -1), (1, 0), (-1, 0))

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls = set(tuple(w) for w in walls)
        guards = set(tuple(g) for g in guards)
        all_cells_number = m * n - len(walls)
        visited = set()

        to_check = [
            (g, d)
            for g in guards
            for d in range(len(Solution.DIRS))
        ]

        while to_check:
            position, direction = to_check.pop()
            visited.add(position)

            new_position = position[0] + Solution.DIRS[direction][0], position[1] + Solution.DIRS[direction][1]
            if 0 <= new_position[0] < m and 0 <= new_position[1] < n and new_position not in guards and new_position not in walls:
                to_check.append((new_position, direction))

        return all_cells_number - len(visited)
