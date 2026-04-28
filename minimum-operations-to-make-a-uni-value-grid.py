class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        modulo = grid[0][0] % x
        counter = Counter()

        for row in grid:
            for cell in row:
                if cell % x != modulo:
                    return -1

                operations = (cell - modulo) // x
                counter[operations] += 1
        
        values = list(sorted(counter.keys()))

        lefts = { values[0]: 0 }
        all_operations = counter[values[0]]
        for prev_value, value in pairwise(values):
            lefts[value] = lefts[prev_value] + all_operations * (value - prev_value)
            all_operations += counter[value]

        rights = { values[-1]: 0 }
        all_operations = counter[values[-1]]
        for prev_value, value in pairwise(reversed(values)):

            rights[value] = rights[prev_value] + all_operations * (prev_value - value)
            all_operations += counter[value]

        return min(lefts[value] + rights[value]
            for value in values)
