class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.groups = n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def unite(self, a: int, b: int) -> bool:
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        self.parent[pb] = pa
        self.groups -= 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        dsu = DSU(n)

        must_strength = []

        must_edges = []
        opt_edges = []

        for e in edges:
            if e[3]:
                must_edges.append(e)
            else:
                opt_edges.append(e)

        for e in must_edges:
            if dsu.unite(e[0], e[1]) == False:
                return -1

            must_strength.append(e[2])

        opt_edges.sort(key=lambda x: x[2] << 1, reverse=True)

        opt_strength = [
            e[2]
            for e in opt_edges
            if dsu.unite(e[0], e[1])
        ]

        if dsu.groups > 1:
            return -1

        opt_strength.sort()

        used = 0
        for i in range(len(opt_strength)):
            if used == k:
                break
            opt_strength[i] *= 2
            used += 1

        return min(chain(must_strength, opt_strength))
