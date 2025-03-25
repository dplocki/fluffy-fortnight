# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        pointing_to_result = ListNode()
        current = pointing_to_result

        while l1 != None or l2 != None or carry > 0:
            tmp = carry
            if l1 != None:
                tmp += l1.val
                l1 = l1.next

            if l2 != None:
                tmp += l2.val
                l2 = l2.next

            current.next = ListNode(tmp % 10)
            carry = tmp // 10

            current = current.next

        return pointing_to_result.next
