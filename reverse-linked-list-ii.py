# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_node = zero_node = ListNode(next=head)
        for _ in range(left - 1):
            left_node = left_node.next

        current = first_to_reversed = left_node.next
        tmp = current
        prev = None

        for _ in range(right - left + 1):
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp

        left_node.next = prev
        first_to_reversed.next = current

        return zero_node.next
