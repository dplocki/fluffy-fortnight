class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = 0
        rest = 0

        if need1 > need2:
            common = need2 * min(costBoth, cost1 + cost2)
            rest = (need1 - need2) * min(costBoth, cost1)
        else:
            common = need1 * min(costBoth, cost1 + cost2)
            rest = (need2 - need1) * min(costBoth, cost2)

        return common + rest
