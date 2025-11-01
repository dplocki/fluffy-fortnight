# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        to_result = ListNode()
        node = head
        tmp = to_result

        while node:
            if node.val not in nums_set:
                tmp.next = node
                tmp = node

            node = node.next

        tmp.next = None

        return to_result.next
