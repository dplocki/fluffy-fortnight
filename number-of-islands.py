class Solution:
    DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def numIslands(self, grid: List[List[str]]) -> int:
        all_lands = set(
            (row_index, column_index)
            for row_index, row in enumerate(grid)
            for column_index, cell in enumerate(row)
            if cell == '1'
        )

        result = 0
        visited = set()
        for start_land in all_lands:
            if start_land in visited:
                continue
            
            result += 1                    
            to_check = [start_land]

            while to_check:
                current = to_check.pop()
                if current in visited:
                    continue

                visited.add(current)

                for d_row, c_row in Solution.DIRECTIONS:
                    point = (current[0] + d_row, current[1] + c_row)
                    if point not in all_lands:
                        continue
                    
                    if point in visited:
                        continue

                    to_check.append(point)

        return result
