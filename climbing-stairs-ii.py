class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        @cache
        def get_minimum_cost(stair: int) -> int:
            if stair < 0:
                return inf
            
            if stair == 0:
                return 0
            
            return min(
                get_minimum_cost(stair - 3) + 9,
                get_minimum_cost(stair - 2) + 4,
                get_minimum_cost(stair - 1) + 1,
            ) + costs[stair - 1]


        return get_minimum_cost(n)
