class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        the_lowest = prices[0]
        the_best = 0

        for price in prices:
            tmp = price - the_lowest
            if tmp > the_best:
                the_best = tmp

            the_lowest = min(the_lowest, price)

        return the_best
