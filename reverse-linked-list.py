# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        new_head = self.reverseList(head.next)

        n = new_head
        while n.next != None:
            n = n.next

        n.next = head
        head.next = None

        return new_head
