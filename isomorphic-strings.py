class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len({*zip(s, t)}) == len(set(s)) == len(set(t))
