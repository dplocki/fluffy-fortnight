class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        the_lowest = prices[0]
        the_best = 0

        for price in prices:
            the_best = max(the_best, price - the_lowest)
            the_lowest = min(the_lowest, price)

        return the_best
