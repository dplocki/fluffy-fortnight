# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        turtle = head
        hare = head.next.next

        while hare != None and hare.next != None:
            turtle = turtle.next
            hare = hare.next.next

        turtle.next = turtle.next.next
        return head
