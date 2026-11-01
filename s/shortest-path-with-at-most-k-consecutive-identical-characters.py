class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        best = [k + 1] * n
        heap = [(0, 1, 0)]

        while heap:
            distance, run, node = heappop(heap)
            if run >= best[node]:
                continue

            if node == n - 1:
                return distance

            best[node] = run
            for start, w in graph[node]:
                new_run = run + 1 if labels[start] == labels[node] else 1
                if new_run < best[start]:
                    heappush(heap, (distance + w, new_run, start))

        return -1
