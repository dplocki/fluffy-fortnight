class Solution:
    DIRECTONS = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, columns = len(heightMap), len(heightMap[0])
        level = 0
        not_visited = set()
        deep_heap = []
        for row_index in range(rows):
            for column_index in range(columns):
                if row_index == 0 or row_index == rows - 1 or column_index == 0 or column_index == columns - 1:
                    heappush(deep_heap, (heightMap[row_index][column_index], row_index, column_index))
                else:
                    not_visited.add((row_index, column_index))

        result = 0
        while deep_heap:
            deep, row_index, column_index = heappop(deep_heap)

            for r_delta, c_delta in Solution.DIRECTONS:
                new_row_index = row_index + r_delta
                new_column_index = column_index + c_delta

                if (new_row_index, new_column_index) not in not_visited:
                    continue

                result += max(0, deep - heightMap[new_row_index][new_column_index])
                not_visited.remove((new_row_index, new_column_index))

                heappush(deep_heap, (max(deep, heightMap[new_row_index][new_column_index]), new_row_index, new_column_index))

        return result
