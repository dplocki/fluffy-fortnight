# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        last_node = head
        elements_number = 1
        for _ in range(k):
            if last_node.next != None:
                last_node = last_node.next
                elements_number += 1
                continue

            return self.rotateRight(head, k % elements_number)

        before_move_node = head
        while last_node.next:
            last_node = last_node.next
            before_move_node = before_move_node.next

        last_node.next = head
        head = before_move_node.next
        before_move_node.next = None

        return head
