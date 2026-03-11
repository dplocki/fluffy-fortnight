class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        minimum = prices[-1]
        stack = [prices[-1]]

        for index in range(len(prices) - 2, -1, -1):
            current = prices[index]
            while stack and stack[-1] > current:
                stack.pop()

            if stack:
                prices[index] -= stack[-1]

            stack.append(current)

        return prices
