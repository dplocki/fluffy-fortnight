class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parents = list(range(n))
        minimums = [inf] * n

        def find(node: int) -> int:
            if parents[node] != node:
                parents[node] = find(parents[node])

            return parents[node]

        for a, b, distance in roads:
            parent_a = find(a - 1)
            parent_b = find(b - 1)

            min_result = min(distance, minimums[parent_a], minimums[parent_b])
            minimums[parent_a] = min_result
            minimums[parent_b] = min_result

            parents[parent_b] = parent_a

        return minimums[find(0)]
