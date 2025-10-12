# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode()
        node = head
        prev = result

        while node != None:
            if node.val != val:
                prev.next = node
                prev = node
            node = node.next
        prev.next = None

        return result.next
