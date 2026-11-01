class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        graph = [[] for _ in range(n)]
        for node, v in edges:
            graph[node].append(v)
            graph[v].append(node)

        masks = [1 << (ord(c) - 97) for c in s]
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        initial = masks[:]
        order = []
        stack = [0]

        while stack:
            node = stack.pop()
            tin[node] = len(order)
            order.append(node)

            for v in graph[node]:
                if v == parent[node]:
                    continue

                parent[v] = node
                depth[v] = depth[node] + 1
                initial[v] ^= initial[node]
                stack.append(v)

        size = [1] * n
        heavy = [-1] * n
        for i in range(n - 1, 0, -1):
            node = order[i]
            p = parent[node]
            size[p] += size[node]
            if heavy[p] == -1 or size[node] > size[heavy[p]]:
                heavy[p] = node

        head = [0] * n
        for i in range(1, n):
            node = order[i]
            p = parent[node]
            head[node] = head[p] if heavy[p] == node else node

        del graph, heavy, order

        fenwick = [0] * (n + 1)


        def toggle(i: int, delta: int) -> None:
            while i <= n:
                fenwick[i] ^= delta
                i += i & -i


        def root_mask(u: int) -> int:
            result = initial[u]
            i = tin[u] + 1
            while i:
                result ^= fenwick[i]
                i -= i & -i
            return result


        result = []
        for query in queries:
            action, a, b = query.split()

            if action == "update":
                node = int(a)
                new_mask = 1 << (ord(b) - 97)
                delta = masks[node] ^ new_mask
                if not delta:
                    continue

                masks[node] = new_mask
                toggle(tin[node] + 1, delta)
                toggle(tin[node] + size[node] + 1, delta)

            elif action == "query":
                u, w = int(a), int(b)
                _from, _to = u, w
                while head[_from] != head[_to]:
                    if depth[head[_from]] > depth[head[_to]]:
                        _from = parent[head[_from]]
                    else:
                        _to = parent[head[_to]]

                lca = _from if depth[_from] < depth[_to] else _to
                mask = root_mask(u) ^ root_mask(w) ^ masks[lca]
                result.append((mask & (mask - 1)) == 0)

        return result
