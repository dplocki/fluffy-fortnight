class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        @cache
        def internal(i: int) -> int:
            if i == n:
                return 0
            
            one, two, three = -inf, -inf, -inf

            if i < n:
                one = stoneValue[i] - internal(i + 1)
            if i + 1 < n:
                two = stoneValue[i] + stoneValue[i + 1] - internal(i + 2)
            if i + 2 < n:
                three = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - internal(i + 3)

            return max(one, two, three)

        result = internal(0)
        if result > 0:
            return 'Alice'
        
        if result < 0:
            return 'Bob'
        
        return 'Tie'
