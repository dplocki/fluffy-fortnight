class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        cost_map = {}
        for start, end, weight in edges:
            if start not in cost_map:
                cost_map[start] = []

            cost_map[start].append((weight, end))

            if end not in cost_map:
                cost_map[end] = []
            
            cost_map[end].append((weight << 1, start))

        to_check = [(0, 0)]
        cost_to_node = {  }

        while to_check:
            current_node, current_cost = to_check.pop()
            if current_node in cost_to_node and current_cost >= cost_to_node.get(current_node):
                continue

            cost_to_node[current_node] = current_cost

            for node_cost, node in cost_map.get(current_node, []):
                new_cost = node_cost + current_cost
                if node in cost_to_node and new_cost >= cost_to_node[node]:
                    continue

                to_check.append((node, new_cost))

        return cost_to_node.get(n - 1, -1)
