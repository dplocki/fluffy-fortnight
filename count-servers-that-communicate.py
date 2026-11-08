class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        result = set()
        occupied_columns = defaultdict(list)

        for r, row in enumerate(grid):
            previous_server_column = None

            for c, cell in enumerate(row):
                if cell == 0:
                    continue
                
                occupied_columns[c].append(r)
                
                if previous_server_column is not None:
                    result.add((r, previous_server_column))
                    result.add((r, c))

                previous_server_column = c

        for c, rows in occupied_columns.items():
            if len(rows) < 2:
                continue
            
            for r in rows:
                result.add((r, c))

        return len(result)
