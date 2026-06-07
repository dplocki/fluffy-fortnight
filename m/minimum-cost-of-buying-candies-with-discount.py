class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        return sum(candy
                for index, candy in enumerate(sorted(cost, reverse=True))
                if index % 3 != 2
            )
