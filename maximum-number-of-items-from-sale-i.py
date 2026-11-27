class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        the_lowest_price = min(price for _, price in items)
        dp = [0] * (budget + 1)

        for factor, price in items:
            item_count = sum(1 for f, _ in items if f % factor == 0)

            for new_price in range(budget, price - 1, -1):
                tmp = dp[new_price - price]
                if tmp + item_count > dp[new_price]:
                    dp[new_price] = tmp + item_count

        return max(
            dp[p] + (budget - p) // the_lowest_price
            for p in range(budget + 1)
        )
