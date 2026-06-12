MOD = 1_000_000_007

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        nodes = defaultdict(set)
        for node_a, node_b in edges:
            nodes[node_a].add(node_b)
            nodes[node_b].add(node_a)
        
        queries_nodes = defaultdict(set)
        for node_a, node_b in queries:
            queries_nodes[node_a].add(node_b)
            queries_nodes[node_b].add(node_a)

        groups = list(range(len(nodes) + 1))

        def find_parent(node: int) -> int:
            if node != groups[node]:
                groups[node] = find_parent(groups[node])

            return groups[node]

        lca = {}
        distance = {}

        def tarjan(a: int, b: int) -> int:
            distance[a] = b
            for n in nodes[a]:
                if n not in distance:
                    tarjan(n, b + 1)
                    groups[n] = a

            for n in queries_nodes[a]:
                if n in distance:
                    lca[a, n] = lca[n, a] = find_parent(n)

        tarjan(1, 0)
        p, mod = [0, 1], MOD
        edges_x = [
            distance[x] + distance[y] - (distance[lca[(x, y)]] << 1) for x, y in queries
        ]

        for _ in range(max(edges_x)):
            p.append( (p[-1] << 1) % mod)

        return [p[i] for i in edges_x]
