DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows, columns = 0, 0
        start = None
        litters = {}

        for row_index, row in enumerate(classroom):
            columns = 0
            for column_index, letter in enumerate(row):
                if letter == 'S':
                    start = row_index, column_index
                elif letter == 'L':
                    litters[row_index, column_index] = None
                
                columns += 1

            rows += 1

        all_litters = 0
        litter_mask = 1
        for key in litters.keys():
            litters[key] = litter_mask
            all_litters |= litter_mask
            litter_mask <<= 1

        best_energy = { (start[0], start[1], 0): energy }
        to_check = deque(((start[0], start[1], 0, energy, 0), ))

        while to_check:
            row, column, litter_mask, current_energy, current_steps = to_check.popleft()

            if litter_mask == all_litters:
                return current_steps

            if current_energy == 0:
                continue

            for dr, dc in DIRS:
                new_row = row + dr
                if 0 > new_row or new_row >= rows:
                    continue

                new_column = column + dc
                if 0 > new_column or new_column >= columns:
                    continue

                if classroom[new_row][new_column] == 'X':
                    continue

                new_energy = energy if classroom[new_row][new_column] == 'R' else current_energy - 1
                new_mask = litter_mask | litters.get((new_row, new_column), 0)

                if new_energy > best_energy.get((new_row, new_column, new_mask), -1):
                    best_energy[new_row, new_column, new_mask] = new_energy
                    to_check.append((new_row, new_column, new_mask, new_energy, current_steps + 1))

        return -1
