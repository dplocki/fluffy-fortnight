class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for buy, sell in pairwise(prices):
            if buy < sell:
                result += sell - buy

        return result
