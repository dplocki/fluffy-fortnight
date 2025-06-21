class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = {i:set() for i in range(n)}

        for ancestor, child in edges:
            parents[child].add(ancestor)

        result = []
        cache = {}
        
        for node in range(n):
            node_ancestors = self.get_all_ancestor(parents, cache, node)
            result.append(list(sorted(node_ancestors)))

        return result

    def get_all_ancestor(self, parents, cache, n):
        if n in cache:
            return cache[n]

        result = set(parents[n])
        for node in parents[n]:
            result |= self.get_all_ancestor(parents, cache, node)

        cache[n] = result
        return result
