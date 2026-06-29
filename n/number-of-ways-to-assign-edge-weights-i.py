MOD = 1_000_000_007

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        nodes = defaultdict(set)
        for node_a, node_b in edges:
            nodes[node_a].add(node_b)
            nodes[node_b].add(node_a)

        nodes_depth = {}
        to_check = [(1, 0)]
        max_depth = 0

        while to_check:
            current_node, current_deep = to_check.pop()
            if current_node in nodes_depth:
                continue
            
            nodes_depth[current_node] = current_deep
            max_depth = max(max_depth, current_deep)

            new_deep = current_deep + 1
            for new_node in nodes[current_node]:
                if new_node in nodes_depth:
                    continue

                to_check.append((new_node, new_deep))

        return pow(2, max_depth - 1, MOD)
