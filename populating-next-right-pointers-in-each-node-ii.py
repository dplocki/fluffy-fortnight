"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        level = [root, None]
        while len(level) > 1:
            new_level = []
            for node, node_next in zip(level, level[1:]):
                node.next = node_next

                if node.left:
                    new_level.append(node.left)

                if node.right:
                    new_level.append(node.right)

            new_level.append(None)
            level = new_level

        return root
