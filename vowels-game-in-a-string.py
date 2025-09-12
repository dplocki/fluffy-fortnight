class Solution:
    VOWELS = set('aeiou')

    def doesAliceWin(self, s: str) -> bool:
        return bool(set(s) & Solution.VOWELS)
