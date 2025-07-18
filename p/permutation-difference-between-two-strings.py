class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sd = { c: i for i, c in enumerate(s) }
        return sum(
            abs(sd[c] - i)
            for i, c in enumerate(t)
        )
