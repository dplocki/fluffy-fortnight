class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        items.sort(key=lambda x: x[1])

        largest_factor = max(factor for factor, _ in items)

        frequency = [0] * (largest_factor + 1)
        for factor, _ in items:
            frequency[factor] += 1

        for index in range(1, largest_factor + 1):
            if frequency[index] == 0:
                continue

            for factor in range(index * 2, largest_factor + 1, index):
                frequency[index] += frequency[factor]

        lowest_price = items[0][1]
        result = 0
        for factor, price in items:
            if price > lowest_price * 2:
                break

            cnt = frequency[factor] - 1
            how_many = min(cnt, budget // price)
            result += how_many * 2
            budget -= how_many * price

        result += budget // lowest_price
        return result
