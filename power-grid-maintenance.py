class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c + 1)
        for u, v in connections:
            uf.union(u, v)

        component_heaps = defaultdict(list)

        for station in range(1, c + 1):
            root = uf.find(station)
            heapq.heappush(component_heaps[root], station)

        offline = set()
        result = []

        for command_type, station in queries:
            if command_type == 1:
                if station not in offline:
                    result.append(station)
                else:
                    root = uf.find(station)
                    heap = component_heaps[root]

                    while heap and heap[0] in offline:
                        heapq.heappop(heap)
                    
                    result.append(heap[0] if heap else -1)
            elif command_type == 2:
                offline.add(station)
            else:
                raise Exception('unknown command')
        
        return result
