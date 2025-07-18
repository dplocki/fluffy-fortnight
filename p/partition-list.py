# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        start_lower_than_x = ListNode()
        lower_than_x = start_lower_than_x
        start_higher_than_x = ListNode()
        higher_than_x = start_higher_than_x

        while head:
            if head.val < x:
                lower_than_x.next = head
                lower_than_x = lower_than_x.next
            else:
                higher_than_x.next = head 
                higher_than_x = higher_than_x.next

            head = head.next
            lower_than_x.next = None
            higher_than_x.next = None

        lower_than_x.next = start_higher_than_x.next
        return start_lower_than_x.next
