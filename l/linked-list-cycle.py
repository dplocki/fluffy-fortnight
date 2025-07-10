# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = hare = head

        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next

            if turtle == hare:
                return True

        return False
