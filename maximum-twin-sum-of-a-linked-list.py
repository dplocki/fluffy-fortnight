# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hare = head
        turtle = head
        while hare is not None:
            turtle = turtle.next
            hare = hare.next.next

        stack = []
        while turtle is not None:
            stack.append(turtle.val)
            turtle = turtle.next

        result = 0
        turtle = head 
        while stack:
            result = max(result, stack.pop() + turtle.val)
            turtle = turtle.next 

        return result
