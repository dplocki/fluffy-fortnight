# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        hare = head
        turtle = head
        previous_turtle = None

        while True:
            if not hare:
                break 

            hare = hare.next
            if not hare:
                break
            hare = hare.next

            previous_turtle = turtle
            turtle = turtle.next

        if previous_turtle:
            previous_turtle.next = None

        return TreeNode(
            turtle.val,
            self.sortedListToBST(head),
            self.sortedListToBST(turtle.next))
