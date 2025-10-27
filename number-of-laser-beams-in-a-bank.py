class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        return sum(
            a * b
            for a, b in pairwise(laser for laser in (row.count('1') for row in bank) if laser > 0))
