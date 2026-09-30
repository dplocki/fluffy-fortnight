# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first_citical_point = None
        prev_critical_point = None
        result = [inf, -1]

        prev_prev_value = prev_value = head.val
        current_index = 1
        node = head.next
        while node:
            if (prev_prev_value > prev_value < node.val) or (prev_prev_value < prev_value > node.val):
                if prev_critical_point:
                    result[0] = min(current_index - 1 - prev_critical_point, result[0])
                else:
                    prev_critical_point = current_index - 1

                prev_critical_point = current_index - 1

                if first_citical_point:
                    result[1] = current_index - 1 - first_citical_point
                else:
                    first_citical_point = current_index - 1

            prev_prev_value = prev_value
            prev_value = node.val
            node = node.next
            current_index += 1

        if isinf(result[0]):
            result[0] = -1

        return result
