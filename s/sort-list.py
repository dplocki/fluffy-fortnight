# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        lower, higher = ListNode(), ListNode()
        tmp_lower, tmp_higher = lower, higher

        tmp = head.next
        while tmp:
            if tmp.val < head.val:
                tmp_lower.next = tmp
                tmp_lower = tmp
            else:
                tmp_higher.next = tmp
                tmp_higher = tmp

            tmp = tmp.next

        tmp_lower.next = None
        tmp_higher.next = None

        result = ListNode()

        result.next = self.sortList(lower.next)

        tmp = result
        while tmp.next:
            tmp = tmp.next

        tmp.next = head
        tmp = tmp.next
        tmp.next = self.sortList(higher.next)

        return result.next
