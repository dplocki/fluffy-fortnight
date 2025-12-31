class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        cells = list(map(tuple, cells))

        def build_map(water_map, current_day, end_day):
            if end_day > current_day:
                water_map.update(cells[current_day:end_day])
            elif end_day < current_day:
                water_map.difference_update(cells[end_day:current_day])

            return water_map

        def can_cross(water_map: Set[Tuple[int, int]]) -> bool:
            to_check = [tile
                for tile in map(lambda c: (1, c), range(1, col + 1))
                if tile not in water_map]
            visited = set()

            while to_check:
                current = to_check.pop()
                if current in visited:
                    continue

                visited.add(current)
                r, c = current

                if r == row:
                    return True

                if r > 1 and (r - 1, c) not in water_map:
                    to_check.append((r - 1, c))

                if (r + 1, c) not in water_map:
                    to_check.append((r + 1, c))

                if c > 1 and (r, c - 1) not in water_map:
                    to_check.append((r, c - 1))
                
                if c < col and (r, c + 1) not in water_map:
                    to_check.append((r, c + 1))

            return False

        left, right = 0, len(cells)
        result = 0
        water_map = set()
        water_map_day = 0

        while left <= right:
            midle = (left + right) >> 1
            water_map = build_map(water_map, water_map_day, midle)
            water_map_day = midle

            if can_cross(water_map):
                left = midle + 1
            else:
                result = midle - 1
                right = midle - 1

        return result
