class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

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

            value %= k 
            if value == 0:
                return result + 1, 0
            
            return result, value

        return interal(0, None)[0]
