class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def interal(node_index: int, parent_index: int) -> Tuple[int, int]:
            value = values[node_index]

            children = (
                interal(child, node_index)
                for child in graph[node_index]
                if child != parent_index
            )

            result = 0
            for child_group_count, child_group_value in children:
                result += child_group_count
                value += child_group_value

            if value % k == 0:
                return result + 1, 0
            
            return result, value % k

        return interal(0, None)[0]
