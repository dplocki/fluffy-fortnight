class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        groups = list(range(n))
        edges_to_group = {}

        def find_root(node: int) -> int:
            if groups[node] == node:
                return node

            group = find_root(groups[node])
            groups[node] = group
            return group

        def merge_group(a: int, b: int) -> int:
            group_a = find_root(a)
            group_b = find_root(b)

            if group_a != group_b:
                edges_to_group[group_a] = edges_to_group.get(group_a, 0) + 1
                
                if group_b in edges_to_group:
                    edges_to_group[group_a] += edges_to_group[group_b]
                    del edges_to_group[group_b]

                groups[group_b] = group_a
            else:
                edges_to_group[group_a] += 1

        for a, b in edges:
            merge_group(a, b)
   
        return sum(1
            for group, count in Counter(find_root(i) for i in range(n)).items()
            if count * (count - 1) >> 1 == edges_to_group.get(group, 0)
        )
