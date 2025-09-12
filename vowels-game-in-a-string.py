class Solution:
    VOWELS = set('aeiou')

    def doesAliceWin(self, s: str) -> bool:
        return sum(1 for l in s if l in Solution.VOWELS) > 0
