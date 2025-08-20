"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        cache = {
            current.val: Node(current.val)
            for current in self.traverse(node)
        }

        for current in self.traverse(node):
            copy_current = cache[current.val]
            for n in current.neighbors:
                copy_current.neighbors.append(cache[n.val])

        return cache[node.val]

    def traverse(self, node):
        to_check = deque([node])
        visited = set()

        while to_check:
            current = to_check.popleft()
            if current in visited:
                continue

            visited.add(current)
            yield current
            for n in current.neighbors:
                if n not in visited:
                    to_check.append(n)
