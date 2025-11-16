class Solution:
    MODULO = int(1e9 + 7)

    def numSub(self, s: str) -> int:
        return sum(map(lambda l: l*(l + 1)//2, map(len, s.split('0')))) % Solution.MODULO
