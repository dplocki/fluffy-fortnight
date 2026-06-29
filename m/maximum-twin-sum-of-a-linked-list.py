# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hare = head
        turtle = head
        stack = []

        while hare is not None:
            stack.append(turtle.val)
            turtle = turtle.next
            hare = hare.next.next

        result = 0
        while turtle:
            result = max(result, stack.pop() + turtle.val)
            turtle = turtle.next

        return result
