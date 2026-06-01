class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        result = 0

        for index, candy in enumerate(sorted(cost, reverse=True)):
            if index % 3 != 2:
                result += candy
        
        return result
