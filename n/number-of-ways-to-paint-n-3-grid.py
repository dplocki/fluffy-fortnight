class Solution:
    MOD = 10**9 + 7

    def numOfWays(self, n: int) -> int:
        aba, abc = 6, 6
        
        for i in range(1, n):
            next_aba = (aba * 3 + abc * 2) % Solution.MOD
            next_abc = (aba * 2 + abc * 2) % Solution.MOD
            aba, abc = next_aba, next_abc
            
        return (aba + abc) % Solution.MOD
