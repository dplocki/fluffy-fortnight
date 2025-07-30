class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        result = 0
        max_pens = total // cost1

        for num_pens in range(max_pens + 1):
            remaining = total - (num_pens * cost1)
            result += (remaining // cost2) + 1

        return result
