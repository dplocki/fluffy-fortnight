class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n = len(s1)
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True

            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False
