# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carring = 0
        result = ListNode()
        current = result

        while l1 != None or l2 != None or carring > 0:
            tmp = carring
            if l1 != None:
                tmp += l1.val
                l1 = l1.next

            if l2 != None:
                tmp += l2.val
                l2 = l2.next

            current.next = ListNode(tmp % 10)
            carring = tmp // 10

            current = current.next

        return result.next
