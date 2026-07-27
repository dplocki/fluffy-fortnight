class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_nodes = sorted(range(n), key=lambda i: nums[i])
        map_node_sorted = [0] * n
        for index, node in enumerate(sorted_nodes):
            map_node_sorted[node] = index

        maximum_jumps = n.bit_length()
        precalculated_distances = [[0] * maximum_jumps for _ in range(n)]

        left = 0
        for node in range(n):
            while left < node and nums[sorted_nodes[node]] - nums[sorted_nodes[left]] > maxDiff:
                left += 1

            precalculated_distances[node][0] = left
        
        for j in range(1, maximum_jumps):
            for i in range(n):
                precalculated_distances[i][j] = precalculated_distances[precalculated_distances[i][j - 1]][j - 1]

        result = []
        for query in queries:
            x, y = map_node_sorted[query[0]], map_node_sorted[query[1]]
            if x > y:
                x, y = y, x

            if x == y:
                result.append(0)
                continue

            step = 0
            for i in range(maximum_jumps - 1, -1, -1):
                if precalculated_distances[y][i] <= x:
                    continue

                y = precalculated_distances[y][i]
                step += 1 << i

            result.append(step + 1 if precalculated_distances[y][0] <= x else -1)

        return result
