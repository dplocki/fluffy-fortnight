class Solution:
    VOWELS = set('aAeEiIoOuU')

    def sortVowels(self, s: str) -> str:
        vowels = iter(sorted(letter
            for letter in s
            if letter in Solution.VOWELS))

        return ''.join(
            next(vowels) if letter in Solution.VOWELS else letter
            for letter in s)
