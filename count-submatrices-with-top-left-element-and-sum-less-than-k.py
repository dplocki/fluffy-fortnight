class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        previous_row = { -1: 0 }
        result = 0

        for row in grid:
            current_row = { -1: 0 }

            for c, cell in enumerate(row):
                current_sum = current_row[c - 1] + previous_row.get(c, 0) + cell - previous_row.get(c - 1, 0)
                current_row[c] = current_sum

                if current_sum > k:
                    break

                result += 1

            previous_row = current_row

        return result
