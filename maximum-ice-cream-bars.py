class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        for index, cost in enumerate(costs):
            if coins < cost:
                return index

            coins -= cost

        return len(costs)
