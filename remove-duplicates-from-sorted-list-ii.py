# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        zero_item = ListNode(0, head)
        prev_node = zero_item
        current = head

        while current:
            while current.next and current.next.val == current.val:
                current = current.next

            if prev_node.next == current:
                prev_node = current
            else:
                prev_node.next = current.next

            current = current.next

        return zero_item.next
