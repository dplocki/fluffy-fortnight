# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        first_result_node = ListNode(0)
        last_result_node = first_result_node
        firsts_nodes = set(node for node in lists if node != None)

        while firsts_nodes:
            minium_node = min(firsts_nodes, key=lambda node: node.val)
            last_result_node.next = minium_node

            firsts_nodes.remove(minium_node)
            if minium_node.next != None:
                firsts_nodes.add(minium_node.next)

            last_result_node = minium_node

        return first_result_node.next
