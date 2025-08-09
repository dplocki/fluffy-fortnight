"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        result_head = Node(0)
        result_node = result_head
        node = head

        while node:
            result_node.next = Node(node.val)
            nodes[node] = result_node.next

            result_node = result_node.next
            node = node.next

        result_node = result_head.next
        node = head
        while node:
            result_node.random = nodes[node.random] if node.random else None

            result_node = result_node.next
            node = node.next

        return result_head.next
