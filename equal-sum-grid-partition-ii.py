class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows, columns = 0, 0
        prefix_table = {}
        values = {}

        for r, row in enumerate(grid):
            rows += 1
            columns = 0

            for c, cell in enumerate(row):
                columns += 1
                prefix_table[r, c] = cell + prefix_table.get((r - 1, c), 0) + prefix_table.get((r, c - 1), 0) - prefix_table.get((r - 1, c - 1), 0)

                if cell not in values:
                    values[cell] = []
                    
                values[cell].append((r, c))

        whole_sum = prefix_table[rows - 1, columns - 1]

        def check_area(end_r: int, end_c: int) -> bool:
            part1_sum = prefix_table[end_r, end_c]
            part2_sum = whole_sum - part1_sum

            if part1_sum == part2_sum:
                return True

            is_single_row = end_r == 0
            is_single_column = end_c == 0

            diffrence = part1_sum - part2_sum
            if diffrence in values:
                for r, c in values[diffrence]:
                    if is_single_row and (0 < c < end_c):
                        continue

                    if is_single_column and (0 < r < end_r):
                        continue

                    if 0 <= r <= end_r and 0 <= c <= end_c:
                        return True

                return False

            diffrence *= -1
            if diffrence not in values:
                return False

            is_single_row = (end_r == rows - 2) or rows == 1
            is_single_column = (end_c == columns - 2) or columns == 1

            for r, c in values[diffrence]:
                if is_single_row and (0 < c < columns - 1):
                    continue

                if is_single_column and (0 < r < rows - 1):
                    continue

                if r > end_r or c > end_c:
                    return True

            return False


        for r in range(rows - 1):
            if check_area(r, columns - 1):
                return True
    
        for c in range(columns - 1):
            if check_area(rows - 1, c):
                return True
        
        return False
