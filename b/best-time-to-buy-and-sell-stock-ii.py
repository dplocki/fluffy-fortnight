class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(
            sell - buy
            for buy, sell in pairwise(prices)
            if buy < sell
        )
