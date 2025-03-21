# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_group_head = head
        last_group_end = ListNode(0, head)

        while True:
            end_node = self.findGroupEnd(new_group_head, k)
            if end_node == None:
                return head

            group_head, group_end = self.reversGroup(new_group_head, end_node)
            last_group_end.next = group_head
            last_group_end = group_end

            if group_end == head:
                head = group_head

            if group_end.next != None:
                new_group_head = group_end.next
            else:
                return head

    def reversGroup(self, head: Optional[ListNode], tail: Optional[ListNode]):
        if head == tail:
            return head, tail

        rest_head, rest_tail = self.reversGroup(head.next, tail)

        head.next = rest_tail.next
        rest_tail.next = head

        return rest_head, head

    def findGroupEnd(self, node: Optional[ListNode], k: int):
        for _ in range(k - 1):
            if node.next == None:
                return None

            node = node.next

        return node
