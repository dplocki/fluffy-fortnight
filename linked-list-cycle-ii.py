# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle = hare = head

        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next

            if turtle == hare:
                break

        if hare == None or hare.next == None:
            return None

        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next

        return tortoise
