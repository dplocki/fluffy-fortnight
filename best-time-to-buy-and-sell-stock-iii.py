class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy = -prices[0]
        first_sell = 0
        second_buy = -prices[0]
        second_sell = 0

        for price in prices[1:]:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)

        return second_sell
