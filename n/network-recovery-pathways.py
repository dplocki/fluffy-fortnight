class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = { i: [] for i in range(n) }
        left_weight, right_weight = inf, 0

        for start, end, cost in edges:
            if not online[start] or not online[end]:
                continue

            graph[start].append((end, cost))
            left_weight = min(left_weight, cost)
            right_weight = max(right_weight, cost)

        def check(minium_weight: int) -> bool:
            node_values = { 0: 0 }
            to_check = [(0, 0)]

            while to_check:
                path_size, node = heappop(to_check)

                if path_size > k:
                    return False

                if node == n - 1:
                    return True

                if node in node_values and path_size > node_values[node]:
                    continue

                for new_node, weight in graph[node]:
                    if weight < minium_weight:
                        continue

                    if (new_node not in node_values) or (node_values[new_node] > node_values[node] + weight):
                        node_values[new_node] = node_values[node] + weight
                        heappush(to_check, (node_values[new_node], new_node))

            return False

        if not check(left_weight):
            return -1

        while left_weight <= right_weight:
            middle_weight = (left_weight + right_weight) >> 1
            if check(middle_weight):
                left_weight = middle_weight + 1
            else:
                right_weight = middle_weight - 1

        return right_weight
