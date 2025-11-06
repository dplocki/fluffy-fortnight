class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        stations = { i: SortedSet([i]) for i in range(1, c + 1) }

        for a, b in connections:
            group = stations[a] | stations[b]
            for i in group:
                stations[i] = group

        for command_type, station in queries:
            group = stations[station]

            if command_type == 1:
                if station in group:
                    result.append(station)
                elif len(group) == 0:
                    result.append(-1)
                else:
                    result.append(group[0])
            elif command_type == 2:
                group.discard(station)
            else:
                raise Exception('unknown command')

        return result
